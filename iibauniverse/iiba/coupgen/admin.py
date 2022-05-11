from django.contrib import admin
from .models import coupon, Coupon_gener

class CouponAdmin(admin.ModelAdmin):
    list_display =['code']


admin.site.register(Coupon_gener)
admin.site.register(coupon)
# Register your models here.
