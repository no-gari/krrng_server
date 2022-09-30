from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.user.views import *

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', UserRegisterView.as_view()),
    path('email_verifier/', EmailVerifierCreateView.as_view()),
    path('only_for_test/', only_for_test),
    path('email_verifier/confirm/', EmailVerifierConfirmView.as_view()),
    path('nickname_create_update/', NicknameCreateUpdateView.as_view()),
    path('find_password/email_verifier/', FindPasswordVerificationView.as_view()),
    path('find_password/email_verifier/confirm/', FindPasswordConfirmView.as_view()),
    path('change_password/<int:pk>/', ChangePasswordView.as_view()),
    path('profile_retrieve_update/<int:pk>/', ProfileRetrieveUpdateView.as_view()),
]
