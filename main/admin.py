from django.contrib import admin
from .models import License, LicenseCategory

class LicenseInline(admin.TabularInline):
    model = License
    extra = 1

@admin.register(LicenseCategory)
class LicenseCategoryAdmin(admin.ModelAdmin):
    inlines = [LicenseInline]

@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'license_number', 'weblink', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'address', 'license_number', 'category__name')
