from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
   path('couponVal',views.couponVal, name='couponVal'),
   path('generatecoupon',views.generatecoupon, name='generate'),
   path('<int:id>/checkingCouponStatus',views.checkingCouponStatus,name='checkingCouponStatus'),  ]