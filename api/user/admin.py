from django.contrib import admin
from api.user.models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileRetrieveUpdateAdmin(admin.ModelAdmin):
    pass
