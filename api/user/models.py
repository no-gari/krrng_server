from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models
from django.dispatch import receiver
import uuid
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _


def directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserManager(DjangoUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.model.normalize_username(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password , **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(verbose_name='이메일', unique=True)
    phone = models.CharField(verbose_name='휴대폰', max_length=11, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']
    VERIFY_FIELDS = ['']  # 회원가입 시 검증 받을 필드 (email, phone)
    REGISTER_FIELDS = ['email', 'password']  # 회원가입 시 입력 받을 필드 (email, phone, password)

    objects = UserManager()

    class Meta:
        verbose_name = '유저'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(verbose_name='닉네임', max_length=32, default='anonymous user')
    profile_pic = models.ImageField(upload_to=directory_path, verbose_name='프로필 사진', null=True, blank=True)
    profile_article = models.CharField(max_length=512, verbose_name='프로필 정보', null=True, blank=True)
    birthday = models.DateField(verbose_name='생일', null=True, blank=True)
    is_creator = models.BooleanField(verbose_name='크리에이터 여부', default=False)

    class SexChoices(models.TextChoices):
        MALE = 'MA', _('남자')
        FEMALE = 'FE', _('여자')

    sex_choices = models.CharField(
        max_length=2,
        choices=SexChoices.choices,
        default=SexChoices.MALE,
    )

    def __str__(self):
        return self.user.username + ' 의 프로필'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile = Profile.objects.create(user=instance)
            profile.save()


class EmailVerifier(models.Model):
    email = models.EmailField(verbose_name='이메일')
    code = models.CharField(verbose_name='인증번호', max_length=6)
    token = models.CharField(verbose_name='토큰', max_length=40)
    created = models.DateTimeField(verbose_name='생성일시')


class PhoneVerifier(models.Model):
    phone = models.CharField(verbose_name='휴대폰번호', max_length=11)
    code = models.CharField(verbose_name='인증번호', max_length=6)
    token = models.CharField(verbose_name='토큰', max_length=40)
    created = models.DateTimeField(verbose_name='생성일시')
