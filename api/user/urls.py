from api.user.views.find_change_user_info import *
from api.user.views.create_update_user import *
from django.urls import path

urlpatterns = [
    # 일반 이메일 로그인 / 회원가입
    path('login/', CustomTokenObtainPairView.as_view()),
    path('email-signup/', UserRegisterView.as_view()),

    # 아이디 중복확인
    path('user-id-check/', UserIdCheckView.as_view()),

    # 가입 시 휴대폰 번호 인증 요청 및 확인
    path('register-phone-create/', RegisterPhoneCreateView.as_view()),
    path('register-phone-confirm/', RegisterPhoneConfirmView.as_view()),

    # 소셜 로그인
    path('social_login/', UserSocialLoginView.as_view()),

    # 아이디 찾기 번호 인증 및 확인
    path('findid-create/', FindIdPhoneCreateView.as_view()),
    path('findid-confirm/', FindIdPhoneConfirmView.as_view()),

    # 비밀번호 찾기 번호 인증 및 확인 및 변경
    path('findpw-create/', FindPasswordPhoneCreateView.as_view()),
    path('findpw-confirm/', FindPasswordPhoneConfirmView.as_view()),
    path('findpw-change/', FindPasswordChangePasswordView.as_view()),

    # 프로필 가져오기
    path('profile/', ProfileView.as_view()),
    # path('profile/', ProfileUpdateView.as_view()),

    # 비밀번호 변경
    path('update/', UserPasswordUpdateView.as_view()),
]
