from api.hospital.models import Hospital
from api.user.models import User
from django.db import models


class HospitalReview(models.Model):
    user = models.ForeignKey(User, verbose_name='유저', on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, verbose_name='병원', on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=128, verbose_name='진료 항목')
    review = models.TextField(verbose_name='리뷰 내용')
    like_users = models.ManyToManyField(User, related_name='like_users', null=True, blank=True, verbose_name='좋아요한 사람들')
    rates = models.FloatField(verbose_name='리뷰 별점', default=5)

    class Meta:
        verbose_name = '병원 리뷰'
        verbose_name_plural = verbose_name


class HospitalRecieptImage(models.Model):
    hospital_review = models.ForeignKey(HospitalReview, verbose_name='리뷰', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='이미지')

    class Meta:
        verbose_name = '병원 영수증 이미지'
        verbose_name_plural = verbose_name


class HospitalReviewImage(models.Model):
    hospital_review = models.ForeignKey(HospitalReview, verbose_name='리뷰', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='이미지')

    class Meta:
        verbose_name = '병원 리뷰 이미지'
        verbose_name_plural = verbose_name
