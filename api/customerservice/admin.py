from .models import FAQ, Offer, FAQMenu, Notice
from django.contrib import admin


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    pass


@admin.register(FAQMenu)
class FAQMenuAdmin(admin.ModelAdmin):
    pass


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    pass


# @admin.register(HospitalReviewReport)
# class HospitalReviewReportAdmin(admin.ModelAdmin):
#     pass
