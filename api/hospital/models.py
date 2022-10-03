from api.user.models import User
from django.db import models


class BestPart(models.Model):
    name = models.CharField(max_length=64, verbose_name='특화 분야')

    class Meta:
        verbose_name = '특화 분야'
        verbose_name_plural = verbose_name


class AvailableAnimal(models.Model):
    animal = models.CharField(max_length=64, verbose_name='진료 동물')

    class Meta:
        verbose_name = '진료 동물'
        verbose_name_plural = verbose_name


class HopitalPrice(models.Model):
    name = models.CharField(max_length=128, verbose_name='진료 항목')
    price = models.CharField(max_length=128, verbose_name='가격')

    class Meta:
        verbose_name = '병원비'
        verbose_name_plural = verbose_name


class Hospital(models.Model):
    name = models.CharField(max_length=64, verbose_name='병원명')
    number = models.CharField(max_length=64, verbose_name='연락처')
    intro = models.TextField(max_length=64, verbose_name='소개글')
    available_time = models.CharField(max_length=512, verbose_name='영업 시간')
    rest_date = models.CharField(max_length=512, verbose_name='휴무일')
    available_animal = models.ManyToManyField(AvailableAnimal, verbose_name='진료 가능 동물')
    best_part = models.ManyToManyField(BestPart, verbose_name='특화 분야')
    hospital_price = models.ManyToManyField(HopitalPrice, verbose_name='병원비')
    is_visible = models.BooleanField(default=True, verbose_name='노출 여부')
    address = models.CharField(max_length=1024, verbose_name='도로명 주소', null=True, blank=True)
    address_detail = models.CharField(max_length=1024, verbose_name='상세 주소', null=True, blank=True)
    latitude = models.CharField(max_length=512, verbose_name='위도', null=True, blank=True)
    longitude = models.CharField(max_length=512, verbose_name='경도', null=True, blank=True)

    class Meta:
        verbose_name = '병원'
        verbose_name_plural = verbose_name


class HospitalImage(models.Model):
    hospital = models.ForeignKey(Hospital, verbose_name='병원', related_name='hospital', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='이미지')

    class Meta:
        verbose_name = '병원 이미지'
        verbose_name_plural = verbose_name


class HospitalReview(models.Model):
    user = models.ForeignKey(User, verbose_name='유저', on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, verbose_name='병원', on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=128, verbose_name='진료 항목')
    receipt = models.ImageField(verbose_name='영수증')
    review = models.TextField(verbose_name='리뷰 내용')
    likes = models.IntegerField(verbose_name='좋아요 수')
    rates = models.FloatField(verbose_name='리뷰 별점', default=5)

    class Meta:
        verbose_name = '병원 리뷰'
        verbose_name_plural = verbose_name


class HospitalReviewImage(models.Model):
    property = models.ForeignKey(HospitalReview, related_name='images', verbose_name='리뷰', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='이미지')

    class Meta:
        verbose_name = '병원 리뷰 이미지'
        verbose_name_plural = verbose_name