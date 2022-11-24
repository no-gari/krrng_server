import random
from django.db import transaction
from rest_framework import serializers
from api.logger.models import PhoneLog
from api.user.validators import validate_password
from api.animal.serializers import AnimalSerializer
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from api.user.models import User, Profile, PhoneVerifier
from django.core.exceptions import ValidationError as DjangoValidationError


# 아이디 찾기 번호 인증
class FindIdPhoneCreateSerializer(serializers.Serializer):
    phone = serializers.CharField()

    def validate(self, attrs):
        phone = attrs['phone']

        if not User.objects.filter(phone=phone).exists():
            raise ValidationError({'phone': ['존재하지 않는 휴대폰입니다.']})

        code = ''.join([str(random.randint(0, 9)) for i in range(6)])

        attrs.update({
            'code': code,
        })

        try:
            self.send_code(attrs)
        except Exception:
            raise ValidationError('인증번호 전송 실패')

        return attrs

    def create(self, attrs):
        return attrs

    def send_code(self, attrs):
        body = f'크르릉 아이디 찾기 인증 번호: %s' % (attrs['code'])
        PhoneLog.objects.create(to=attrs['phone'], body=body)


# 아이디 찾기 휴대폰 번호 인증 확인
class FindIdPhoneConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneVerifier
        fields = ['phone', 'code']


# 비밀번호 찾기 번호 인증
class FindPasswordPhoneCreateSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    phone = serializers.CharField()
    code = serializers.CharField(read_only=True)

    def validate(self, attrs):
        phone = attrs['phone']
        user_id = attrs['user_id']
        email = user_id + '@krrng.com'

        if not User.objects.filter(phone=phone).exists():
            raise ValidationError({'phone': ['존재하지 않는 휴대폰입니다.']})

        if User.objects.filter(email=email).last().phone != phone:
            raise ValidationError({'phone': ['회원정보가 일치하지 않습니다.']})

        code = ''.join([str(random.randint(0, 9)) for i in range(6)])

        attrs.update({
            'code': code,
        })

        try:
            self.send_code(attrs)
        except Exception:
            raise ValidationError('인증번호 전송 실패')

        return attrs

    def create(self, attrs):
        return attrs

    def send_code(self, attrs):
        body = f'크르릉 비밀번호 찾기 인증 번호: %s' % (attrs['code'])
        PhoneLog.objects.create(to=attrs['phone'], body=body)


# 비밀번호 찾기 휴대폰 번호 인증 확인
class FindPasswordPhoneConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneVerifier
        fields = ['phone', 'code']

    def create(self, attrs):
        return attrs


# 비밀번호 찾기 후 비밀번호 변경
class FindPasswordChangePasswordSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()

    def create(self, attrs):
        return attrs


# 닉네임, 생년월일, 성별, 프로필 사진 변경 및 가져오기
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['nickname', 'profile_image', 'birthday', 'sex_choices']


class ProfileRetrieveSerializer(serializers.ModelSerializer):
    animals = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = ['nickname', 'profile_image', 'birthday', 'sex_choices', 'animals']

    def get_animals(self, obj):
        user_animals = obj.user.animal_set.all()
        return AnimalSerializer(user_animals, many=True).data


# 그냥 마이페이지에서 비밀번호 변경
class UserPasswordUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, allow_blank=True)

    class Meta:
        model = User
        fields = ['password']

    def validate(self, attrs):
        password = attrs.get('password')
        errors = {}

        # 비밀번호 검증
        if password:
            try:
                validate_password(password)
            except DjangoValidationError as error:
                errors['password'] = list(error)
            attrs['password'] = make_password(password)
        else:
            attrs['password'] = self.instance.password

        if errors:
            raise ValidationError(errors)

        return attrs

    @transaction.atomic
    def update(self, instance, validated_data):
        instance.__dict__.update(validated_data)
        instance.save()
        return instance
