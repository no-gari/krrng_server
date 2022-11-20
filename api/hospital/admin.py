from django.contrib import admin
from .models import Hospital, HospitalPrice, BestPart, AvailableAnimal, HospitalImage
from django.conf import settings
import requests


class HospitalImageAdmin(admin.StackedInline):
    model = HospitalImage


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    readonly_fields = ('latitude', 'longitude',)
    inlines = (HospitalImageAdmin, )

    def save_model(self, request, obj, form, change):
        naver_client_id = settings.NAVER_CLIENT_ID
        naver_client_secret = settings.NAVER_CLIENT_SECRET
        end_point = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'

        try:
            target = obj.address
            end_point_target = end_point + f'?query={target}'

            headers = {
                "X-NCP-APIGW-API-KEY-ID": naver_client_id,
                "X-NCP-APIGW-API-KEY": naver_client_secret,
                "Accept": "application/json"
            }
            res = requests.get(end_point_target, headers=headers)
            if res.status_code != 200:
                raise Exception()
            res_json = res.json()
            latitude = res_json['addresses'][0]['y']
            longitude = res_json['addresses'][0]['x']

            obj.latitude = latitude
            obj.longitude = longitude
            obj.save()
        except:
            pass
        obj.save()


@admin.register(HospitalPrice)
class HospitalPriceAdmin(admin.ModelAdmin):
    pass


# @admin.register(BestPart)
# class BestPartAdmin(admin.ModelAdmin):
#     pass


@admin.register(AvailableAnimal)
class AvailableAnimalAdmin(admin.ModelAdmin):
    pass
