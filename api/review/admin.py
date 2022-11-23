from django.contrib import admin
from .models import HospitalReview, HospitalReviewImage, HospitalRecieptImage


class HospitalReviewImageAdmin(admin.StackedInline):
    model = HospitalReviewImage


class HospitalRecieptImageAdmin(admin.StackedInline):
    model = HospitalRecieptImage


@admin.register(HospitalReview)
class HospitalPriceAdmin(admin.ModelAdmin):
    inlines = (HospitalReviewImageAdmin, HospitalRecieptImageAdmin, )
