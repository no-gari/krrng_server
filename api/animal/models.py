from django.utils.translation import gettext_lazy as _
from api.user.models import User
from django.db import models


class Animal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='유저')
    name = models.CharField(max_length=64, verbose_name='이름')
    sort = models.CharField(max_length=32, verbose_name='종류')
    birthday = models.DateField(verbose_name='생일', null=True, blank=True)
    weight = models.CharField(max_length=10, verbose_name='몸무게')
    kind = models.CharField(max_length=32, verbose_name='품종')
    hospital_address = models.CharField(max_length=1024, verbose_name='내원 병원 주소')
    hospital_address_detail = models.CharField(max_length=1024, verbose_name='내원 병원 상세주소', null=True, blank=True)
    interested_disease = models.CharField(max_length=128, verbose_name='관심 질병')
    image = models.ImageField(null=True, blank=True, verbose_name='반려동물 이미지')

    class NeuterChoices(models.TextChoices):
        IS_NETURED = 'IS', _('유')
        NOT_NETURED = 'NT', _('무')
        DONT_KNOW = 'DO', _('모름')

    neuter_choices = models.CharField(
        max_length=2,
        choices=NeuterChoices.choices,
        default=NeuterChoices.IS_NETURED,
        verbose_name='중성화 여부'
    )

    has_alergy = models.CharField(
        max_length=2,
        choices=NeuterChoices.choices,
        default=NeuterChoices.IS_NETURED,
        verbose_name='알러지 유무 여부'
    )

    class SexChoices(models.TextChoices):
        MALE = 'MA', _('남자')
        FEMALE = 'FE', _('여자')

    sex_choices = models.CharField(
        max_length=2,
        choices=SexChoices.choices,
        default=SexChoices.MALE,
        verbose_name='성별'
    )

    class Meta:
        verbose_name = '반려동물 정보'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.profile_set.last().nickname + '의 반려동물'
