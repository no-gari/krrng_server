from rest_framework import status
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from api.user.serializers.find_change_user_info import *
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, RetrieveAPIView


# 아이디 찾기 번호 인증
class FindIdPhoneCreateView(CreateAPIView):
    serializer_class = FindIdPhoneCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if serializer.data.get('error') is None:
            return Response(status=status.HTTP_200_OK)


# 아이디 찾기 휴대폰 번호 인증 확인
class FindIdPhoneConfirmView(CreateAPIView):
    serializer_class = FindIdPhoneConfirmSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        phone = serializer.data.get('phone')
        code = serializer.data.get('code')
        user_phone_code = PhoneVerifier.objects.filter(phone=phone).last().code
        if code == user_phone_code and serializer.data.get('error') is None:
            user_email = User.objects.get(phone=phone).email
            user_id = user_email.split('@')[0]
            return Response({'user_id': user_id}, status=status.HTTP_200_OK)


# 비밀번호 찾기 번호 인증
class FindPasswordPhoneCreateView(CreateAPIView):
    serializer_class = FindPasswordPhoneCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if serializer.data.get('error') is None:
            phone_verifier = PhoneVerifier.objects.create(phone=serializer.data.get('phone'), code=serializer.data.get('code'))
            phone_verifier.save()
            return Response(status=status.HTTP_200_OK)


# 비밀번호 찾기 번호 인증 확인
class FindPasswordPhoneConfirmView(CreateAPIView):
    serializer_class = FindPasswordPhoneConfirmSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        phone = serializer.data.get('phone')
        code = serializer.data.get('code')
        user_phone_code = PhoneVerifier.objects.filter(phone=phone).last().code
        if code == user_phone_code and serializer.data.get('error') is None:
            return Response(status=status.HTTP_200_OK)


# 비밀번호 찾기 후 비밀번호 변경
class FindPasswordChangePasswordView(CreateAPIView):
    serializer_class = FindPasswordChangePasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        phone = serializer.data.get('phone')
        password = serializer.data.get('password')
        if serializer.data.get('error') is None:
            user = User.objects.get(phone=phone)
            user.password = make_password(password)
            user.save()
            return Response(status=status.HTTP_200_OK)


# 프로필 가져오기
class ProfileRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProfileRetrieveSerializer
    permission_classes = [IsAuthenticated]
    allowed_methods = ['GET']

    def get_queryset(self):
        return Profile.objects.all().prefetch_related('animal_set', 'user')

    def get_object(self):
        return Profile.objects.get(user=self.request.user)


# 닉네임, 생년월일, 성별, 프로필 사진 변경 및 가져오기
class ProfileUpdateAPIView(UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    allowed_methods = ['PATCH']
    lookup_field = 'pk'

    def get_object(self):
        return Profile.objects.get(user=self.request.user)


@api_view(['POST'])
def userPasswordUpdate(request):
    password = request.POST.get('password')
    user = request.user
    user.password = make_password(password)
    user.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def redirectOneLink(request):
    return redirect('https://onelink.to/82ttrz/')
