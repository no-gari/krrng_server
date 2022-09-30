from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from django.core.exceptions import ValidationError as DjangoValidationError
from api.user.serializers import UserRegisterSerializer, EmailVerifierCreateSerializer, \
    EmailVerifierConfirmSerializer, NicknameCreateUpdateSerializer, FindPasswordVerifierCreateSerializer, \
    FindPasswordVerifierConfirmSerializer, ChangePasswordSerializer, ProfileSerializers
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import User, Profile
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse

# class UserSocialLoginView(CreateAPIView): ## 소셜 로그인 부분
#     serializer_class = UserSocialLoginSerializer


def only_for_test(request):
    return JsonResponse({
        'store' : '이마트',
        'store_region' : '성동점',
        'wine_name' : '개조아 와인',
        'wine_sort' : '레드',
        'wine_grape' : '메를로',
        'wine_price' : '30,000',
        'wine_food' : '스테이크',
        'priority' : '1'
    }, json_dumps_params = {'ensure_ascii': True})


class UserRegisterView(CreateAPIView): ## 회원가입.
    serializer_class = UserRegisterSerializer


class EmailVerifierCreateView(CreateAPIView): ## 이메일 토큰 생성.
    serializer_class = EmailVerifierCreateSerializer


class EmailVerifierConfirmView(CreateAPIView): ## 토큰 유효성 검사.
    serializer_class = EmailVerifierConfirmSerializer


class NicknameCreateUpdateView(CreateAPIView): ## 개인 아이디(닉네임) 생성
    queryset = Profile.objects.all()
    serializer_class = NicknameCreateUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        profile = Profile.objects.get(user_id=self.request.user.id)

        if profile.nickname == 'anonymous user':
            profile.nickname = data['nickname']
            try:
                profile.birthday = data['birthday']
                profile.sex_choices = data['sex_choices']
            finally:
                profile.save()
            return Response({'msg': '등록이 성공적으로 끝났습니다.'})
        else:
            profile.nickname = data['nickname']
            profile.save()
            return Response({'msg': '수정이 완료 되었습니다.'})


class FindPasswordVerificationView(CreateAPIView):
    serializer_class = FindPasswordVerifierCreateSerializer


class FindPasswordConfirmView(CreateAPIView):
    serializer_class = FindPasswordVerifierConfirmSerializer


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()
    lookup_field = 'pk'
    http_method_names = ['patch',]

    def update(self, request, *args, **kwargs):
       instance = self.get_object()
       serializer = self.get_serializer(instance, data=request.data, partial=True)
       serializer.is_valid(raise_exception=True)
       self.perform_update(serializer)
       result = {
        "msg": "성공적으로 변경되었습니다.",
        "status": 200,
       }
       return Response(result)


class ProfileRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializers
    queryset = Profile.objects.all()
    lookup_field = 'pk'
    http_method_names = ['get', 'patch']

    def update(self, request, pk, format=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        result = {
            "msg": "성공적으로 변경되었습니다.",
            "status": 200,
        }
        return Response(result)
#
#
# class LogoutView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)