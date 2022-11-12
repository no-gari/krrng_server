from django.db import models
from api.user.models import User
from api.hospital.models import HospitalReview


class Notice(models.Model):
    name = models.CharField(max_length=1024, verbose_name='공지사항 제목')
    content = models.TextField(verbose_name='공지사항 내용')
    created_at = models.DateField(auto_now_add=True, verbose_name='생성 시간')

    class Meta:
        verbose_name = '공지사항'
        verbose_name_plural = verbose_name


class FAQMenu(models.Model):
    name = models.CharField(max_length=128, verbose_name='FAQ 카테고리')

    class Meta:
        verbose_name = 'FAQ 카테고리'
        verbose_name_plural = verbose_name


class FAQ(models.Model):
    faq_menu = models.ForeignKey(FAQMenu, verbose_name='FAQ 카테고리', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '자주 묻는 질문'
        verbose_name_plural = verbose_name


class Offer(models.Model):
    OFFER_STATUS = (
        ('O', '접수'),
        ('C', '확인완료'),
    )
    hospital_name = models.CharField(max_length=128, verbose_name='병원 업체명')
    hospital_address = models.CharField(max_length=1024, verbose_name='병원 주소명')
    user_name = models.CharField(max_length=128, verbose_name='신청자 명')
    user_email = models.CharField(max_length=256, verbose_name='신청자 이메일')
    user_phone = models.CharField(max_length=128, verbose_name='신청자 전화번호')
    user_hospital = models.CharField(max_length=128, verbose_name='신청자 소속')
    user_level = models.CharField(max_length=128, verbose_name='신청자 직책')
    methods = models.CharField(max_length=128, verbose_name='제휴 및 문의 경로')
    condition = models.CharField(max_length=1, verbose_name='상태', choices=OFFER_STATUS)
    additional_info = models.TextField(verbose_name='비고')

    class Meta:
        verbose_name = '제휴 및 광고 문의'
        verbose_name_plural = verbose_name


class HospitalReviewReport(models.Model):
    OFFER_STATUS = (
        ('O', '접수'),
        ('C', '확인완료'),
    )
    user = models.ForeignKey(User, verbose_name='유저', on_delete=models.CASCADE)
    review = models.ForeignKey(HospitalReview, verbose_name='리뷰', on_delete=models.CASCADE)
    condition = models.CharField(max_length=1, verbose_name='상태', choices=OFFER_STATUS)

    class Meta:
        verbose_name = '병원 리뷰 신고'
        verbose_name_plural = verbose_name


class HospitalReviewReportImage(models.Model):
    property = models.ForeignKey(HospitalReviewReport, related_name='images', verbose_name='리뷰', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='이미지')

    class Meta:
        verbose_name = '병원 리뷰 신고 이미지'
        verbose_name_plural = verbose_name