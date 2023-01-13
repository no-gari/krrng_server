import datetime
import random
from django.db import transaction
from api.logger.models import PhoneLog
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from api.user.models import User, Profile, PhoneVerifier, SocialKindChoices


# 아이디 중복 확인
class UserIdCheckSerializer(serializers.Serializer):
    user_id = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('user_id') + '@krrng.com'

        if User.objects.filter(email=email).exists():
            raise ValidationError({'email': ['이미 가입된 이메일입니다.']})
        return attrs

    def create(self, attrs):
        return attrs


# 휴대폰 번호 인증요청
class RegisterPhoneCreateSerializer(serializers.Serializer):
    phone = serializers.CharField()
    code = serializers.CharField(read_only=True)

    def validate(self, attrs):
        phone = attrs['phone']
        if User.objects.filter(phone=phone).exists():
            raise ValidationError({'phone': ['이미 존재하는 휴대폰입니다.']})
        code = ''.join([str(random.randint(0, 9)) for i in range(6)])
        attrs.update({'code': code})
        try:
            self.send_code(attrs)
        except Exception:
            raise ValidationError('인증번호 전송 실패')
        return attrs

    def create(self, attrs):
        return attrs

    def send_code(self, attrs):
        body = f'크르릉 가입 인증 번호: %s' % (attrs['code'])
        PhoneLog.objects.create(to=attrs['phone'], body=body)


# 가입 시 휴대폰 번호 인증 확인
class RegisterPhoneConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneVerifier
        fields = ['phone', 'code']

    def create(self, attrs):
        return attrs


# 회원가입
class UserRegisterSerializer(serializers.Serializer):
    user_id = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    @transaction.atomic
    def create(self, validated_data):
        user_id = validated_data['user_id']
        if len(user_id.split('@')) == 2:
            user = User.objects.get(email=user_id)
            user.phone = validated_data['phone']
            user.save()
        else:
            email = validated_data['user_id'] + '@krrng.com'
            password = validated_data['password']
            phone = validated_data['phone']
            user, created = User.objects.get_or_create(email=email, password=make_password(password), phone=phone)

            if created:
                user_profile = Profile.objects.create(user=user, nickname=validated_data['user_id'])
                user_profile.save()

        refresh = RefreshToken.for_user(user)
        return {
            'access': refresh.access_token,
            'refresh': refresh,
        }


# 회원가입
class UserTempRegisterSerializer(serializers.Serializer):
    user_id = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    @transaction.atomic
    def create(self, validated_data):
        user_id = validated_data['user_id']
        if len(user_id.split('@')) == 2:
            user = User.objects.get(email=user_id)
            user.phone = validated_data['phone']
            user.save()
        else:
            email = validated_data['user_id'] + '@krrng.com'
            password = validated_data['password']
            user, created = User.objects.get_or_create(email=email, password=make_password(password))

            if created:
                user_profile = Profile.objects.create(user=user, nickname=validated_data['user_id'], birthday=datetime.date.today())
                user_profile.save()

        refresh = RefreshToken.for_user(user)
        return {
            'access': refresh.access_token,
            'refresh': refresh,
        }


# 소셜 로그인
class UserSocialLoginSerializer(serializers.Serializer):
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    code = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)
    nickname = serializers.CharField(write_only=True)
    social_type = serializers.CharField(write_only=True)

    def validate(self, attrs):
        code = attrs['code']
        email = attrs['email']
        nickname = attrs['nickname']
        social_type = attrs['social_type']

        if social_type not in SocialKindChoices:
            raise ValidationError({'kind': '지원하지 않는 소셜 타입입니다.'})

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        code = validated_data['code']
        email = validated_data['email']
        nickname = validated_data['nickname']
        social_type = validated_data['social_type']
        user, created = User.objects.get_or_create(email=email, defaults={'password': make_password(None)})

        if created:
            user_profile = Profile.objects.create(user=user, nickname=nickname, kind=social_type, code=code, birthday=datetime.date.today())
            user_profile.save()

        refresh = RefreshToken.for_user(user)
        return {
            'access': refresh.access_token,
            'refresh': refresh,
        }


class CustomTokenObtainPairSerializer(serializers.Serializer):
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    user_id = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs['user_id'] + '@krrng.com'
        password = attrs['password']
        user = authenticate(email=email, password=password)
        if not user is not None:
            raise ValidationError()

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        email = validated_data['user_id'] + '@krrng.com'
        user = User.objects.get(email=email)
        refresh = RefreshToken.for_user(user)
        return {
            'access': refresh.access_token,
            'refresh': refresh,
        }
