from .models import FAQ, Offer, HospitalReviewReport
from django.contrib import admin


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    pass


@admin.register(HospitalReviewReport)
class HospitalReviewReportAdmin(admin.ModelAdmin):
    pass
