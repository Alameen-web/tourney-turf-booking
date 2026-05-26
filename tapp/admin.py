from django.contrib import admin

from .models import District, Feedback, Locations, Login, Package, PBooking, Turf, TurfComplaint, User


@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ("username", "role")
    search_fields = ("username",)
    list_filter = ("role",)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    search_fields = ("district",)


@admin.register(Locations)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("location", "district")
    list_filter = ("district",)
    search_fields = ("location", "district__district")


@admin.register(Turf)
class TurfAdmin(admin.ModelAdmin):
    list_display = ("turf_name", "turf_phone", "district", "locations", "status")
    list_filter = ("status", "district")
    search_fields = ("turf_name", "turf_ownername", "turf_email")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_phone", "user_email", "status")
    list_filter = ("status", "district")
    search_fields = ("user_name", "user_email", "user_phone")


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("pack_name", "pack_turf", "pack_rate", "pack_type", "pack_status")
    list_filter = ("pack_status", "pack_turf")
    search_fields = ("pack_name", "pack_turf__turf_name")


@admin.register(PBooking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("package", "user", "turf", "date", "status")
    list_filter = ("status", "date")
    search_fields = ("user__user_name", "turf__turf_name", "package__pack_name")


admin.site.register(Feedback)
admin.site.register(TurfComplaint)
