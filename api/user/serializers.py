import hashlib, random, secrets, string, requests

from django.conf import settings
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from api.user.models import User, Profile, EmailVerifier, PhoneVerifier
from api.user.validators import validate_password, string_trim_validator, ascii_username_validator,\
    custom_length_validator, email_verifier
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.hashers import check_password


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True, required=False)
    email_token = serializers.CharField(write_only=True, required=False)
    phone = serializers.CharField(write_only=True, required=False)
    phone_token = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)
    password_confirm = serializers.CharField(write_only=True, required=False)

    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def get_fields(self):
        fields = super().get_fields()

        if 'email' in User.VERIFY_FIELDS:
            fields['email_token'].required = True
        if 'email' in User.VERIFY_FIELDS or 'email' in User.REGISTER_FIELDS:
            fields['email'].required = True
        if 'phone' in User.VERIFY_FIELDS:
            fields['phone_token'].required = True
        if 'phone' in User.VERIFY_FIELDS or 'phone' in User.REGISTER_FIELDS:
            fields['phone'].required = True
        if 'password' in User.REGISTER_FIELDS:
            fields['password'].required = True
            fields['password_confirm'].required = True

        return fields

    def validate(self, attrs):
        email = attrs.get('email')
        email_token = attrs.pop('email_token', None)
        phone = attrs.get('phone')
        phone_token = attrs.pop('phone_token', None)

        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm', None)

        if 'email' in User.VERIFY_FIELDS:
            # 이메일 토큰 검증
            try:
                self.email_verifier = EmailVerifier.objects.get(email=email, token=email_token)
            except EmailVerifier.DoesNotExist:
                raise ValidationError('이메일 인증을 진행해주세요.')
        if 'email' in User.VERIFY_FIELDS or 'email' in User.REGISTER_FIELDS:
            # 이메일 검증
            if User.objects.filter(email=email).exists():
                raise ValidationError({'email': ['이미 가입된 이메일입니다.']})

        if 'phone' in User.VERIFY_FIELDS:
            # 휴대폰 토큰 검증
            try:
                self.phone_verifier = PhoneVerifier.objects.get(phone=phone, token=phone_token)
            except PhoneVerifier.DoesNotExist:
                raise ValidationError('휴대폰 인증을 진행해주세요.')
        if 'phone' in User.VERIFY_FIELDS or 'phone' in User.REGISTER_FIELDS:
            # 휴대폰 검증
            if User.objects.filter(phone=phone).exists():
                raise ValidationError({'phone': ['이미 가입된 휴대폰입니다.']})

        if 'password' in User.REGISTER_FIELDS:
            errors = {}
            # 비밀번호 검증
            if password != password_confirm:
                errors['password'] = ['비밀번호가 일치하지 않습니다.']
                errors['password_confirm'] = ['비밀번호가 일치하지 않습니다.']
            else:
                try:
                    validate_password(password)
                except DjangoValidationError as error:
                    errors['password'] = list(error)
                    errors['password_confirm'] = list(error)

            if errors:
                raise ValidationError(errors)

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data,
        )
        if 'email' in User.VERIFY_FIELDS:
            self.email_verifier.delete()
        if 'phone' in User.VERIFY_FIELDS:
            self.phone_verifier.delete()

        refresh = RefreshToken.for_user(user)

        return {
            'access': refresh.access_token,
            'refresh': refresh,
        }


class EmailVerifierCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerifier
        fields = ['email']

    def validate(self, attrs):
        email_to = attrs['email']

        if User.objects.filter(email=email_to).exists():
            raise ValidationError({'email': ['이미 존재하는 이메일입니다.']})

        code = ''.join([str(random.randint(1, 9)) for i in range(6)])
        created = timezone.now()
        hash_string = str(email_to) + code + str(created.timestamp())
        token = hashlib.sha1(hash_string.encode('utf-8')).hexdigest()

        attrs.update({
            'code': code,
            'token': token,
            'created': created,
        })

        try:
            msg = EmailMessage('Cluv 인증번호 발급',
                               str(code), to=[email_to])
            msg.send()
        except Exception:
            raise ValidationError('인증번호 전송 실패')

        return attrs

    def send_code(self, attrs):
        pass


class EmailVerifierConfirmSerializer(serializers.ModelSerializer):
    email = serializers.EmailField
    code = serializers.CharField(write_only=True)
    email_token = serializers.CharField(read_only=True, source='token')

    class Meta:
        model = EmailVerifier
        fields = ['email', 'code', 'email_token']

    def validate(self, attrs):
        email = attrs['email']
        code = attrs['code']
        try:
            email_verifier = self.Meta.model.objects.get(email=email, code=code)
        except self.Meta.model.DoesNotExist:
            raise ValidationError({'code': ['인증번호가 일치하지 않습니다.']})

        attrs.update({'token': email_verifier.token})
        return attrs

    def create(self, validated_data, *args, **kwargs):
        return validated_data


class NicknameCreateUpdateSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField()

    class Meta:
        model = Profile
        fields = ['id', 'nickname', 'birthday', 'sex_choices']

    def create(self, validated_data):
        return validated_data


class FindPasswordVerifierCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerifier
        fields = ['email']

    def validate(self, attrs):
        email_to = attrs['email']

        if not User.objects.filter(email=email_to).exists():
            raise ValidationError({'email': ['가입되지 않은 이메일입니다.']})

        code = ''.join([str(random.randint(1, 9)) for i in range(6)])
        created = timezone.now()
        hash_string = str(email_to) + code + str(created.timestamp())
        token = hashlib.sha1(hash_string.encode('utf-8')).hexdigest()

        attrs.update({
            'code': code,
            'token': token,
            'created': created,
        })

        try:
            msg = requests.post(
        		"https://api.mailgun.net/v3/sandbox97825590c11a4f5e8431798ffbf0fe5d.mailgun.org/messages",
        		auth=("api", "302b470527bf17f74f7127af6ef0fe80-4de08e90-e60a59fe"),
        		data={"from": "no-reply<mail@dailyz.me>",
    			"to": [email_to],
    			"subject": code,
	    		"text": code})
        except Exception:
            raise ValidationError('인증번호 전송 실패')

        return attrs

    def send_code(self, attrs):
        pass


class FindPasswordVerifierConfirmSerializer(serializers.ModelSerializer):
    email = serializers.EmailField
    code = serializers.CharField(write_only=True)
    temporary_password = serializers.CharField(read_only=True)

    class Meta:
        model = EmailVerifier
        fields = ['email', 'code', 'temporary_password']

    def validate(self, attrs):
        email = attrs['email']
        code = attrs['code']
        try:
            email_verifier_obj = self.Meta.model.objects.get(email=email, code=code)
        except self.Meta.model.DoesNotExist:
            raise ValidationError({'code': ['인증번호가 일치하지 않습니다.']})
        user = User.objects.get(email=email)
        alphabet = string.ascii_letters + string.digits
        temporary_password = ''.join(secrets.choice(alphabet) for i in range(8))
        user.set_password(raw_password=temporary_password)
        user.save()
        email_verifier_obj.delete()
        attrs.update({'temporary_password': temporary_password})

        return attrs

    def create(self, validated_data, *args, **kwargs):
        return validated_data


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    new_password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password_confirm', 'new_password']

    def validate(self, attrs):
        old_password = attrs['old_password']
        new_password = attrs['new_password']
        new_password_confirm = attrs['new_password_confirm']
        user = self.instance
        if check_password(old_password, user.password) is False:
            raise ValidationError({'msg' : '기존 비밀번호를 다시 확인해 주세요.'})
        if new_password == new_password_confirm and validate_password(new_password) is True:
            user.set_password(raw_password=new_password)
            user.save()
        return attrs


class ProfileSerializers(serializers.ModelSerializer):
    profile_pic = serializers.CharField()
    nickname = serializers.CharField()
    profile_article = serializers.CharField()

    class Meta:
        model = Profile
        fields = ['profile_pic', 'nickname', 'profile_article']

    def validate(self, attrs, *args, **kwargs):
        contents = attrs['contents']
        user_id = self.request.user.id
        return attrs

    def update(self, validated_data, *args, **kwargs):
        return validated_data