from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.user.serializers.create_update_user import *
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status


# 아이디 중복 확인
class UserIdCheckView(CreateAPIView):
    serializer_class = UserIdCheckSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if serializer.data.get('error') is None:
            return Response(status=status.HTTP_200_OK)


# 휴대폰 번호 인증요청
class RegisterPhoneCreateView(CreateAPIView):
    serializer_class = RegisterPhoneCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if serializer.data.get('error') is None:
            phone_verifier = PhoneVerifier.objects.create(phone=serializer.data.get('phone'), code=serializer.data.get('code'))
            phone_verifier.save()
            return Response(status=status.HTTP_200_OK)


# 휴대폰 번호 인증 확인
class RegisterPhoneConfirmView(CreateAPIView):
    serializer_class = RegisterPhoneConfirmSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        phone = serializer.data.get('phone')
        code = serializer.data.get('code')
        user_phone_code = PhoneVerifier.objects.filter(phone=phone).last().code
        if code == user_phone_code and serializer.data.get('error') is None:
            return Response(status=status.HTTP_200_OK)


# 소셜 로그인
class UserSocialLoginView(CreateAPIView):
    serializer_class = UserSocialLoginSerializer


# 일반 로그인
class CustomTokenObtainPairView(CreateAPIView):
    serializer_class = CustomTokenObtainPairSerializer


# 일반 회원가입
class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.create(request, *args, **kwargs)
        if serializer.status_code == 201:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return serializer
