from django.contrib import admin
from .models import Department, DepartmentMember


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at", "is_active")
    search_fields = ("name",)


class DepartmentMemberAdmin(admin.ModelAdmin):
    list_display = ("department", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)


admin.site.register(DepartmentMember, DepartmentMemberAdmin)
admin.site.register(Department, DepartmentAdmin)
