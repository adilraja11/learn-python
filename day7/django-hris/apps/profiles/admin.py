from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "updated_at")


admin.site.register(Profile, ProfileAdmin)
