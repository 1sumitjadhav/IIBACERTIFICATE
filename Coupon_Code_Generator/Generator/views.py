from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Coupon 


def home(request):
    # coupon_ge= Coupon.objects.all()
    if request.method =="POST":
        for j in range(0,50):
            code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            coupon_code = ''
            for i in range(0, 7):
                slice_start = random.randint(0, len(code_chars) - 1)
                coupon_code += code_chars[slice_start: slice_start + 1]
            print(coupon_code)
            coupon_ge =Coupon(code= coupon_code)
            coupon_ge.save()

    return render(request,'index.html')

