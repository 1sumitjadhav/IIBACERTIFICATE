from django.contrib import admin
from .models import Coupon

class CouponAdmin(admin.ModelAdmin):
    list_display =['code']


admin.site.register(Coupon, CouponAdmin)