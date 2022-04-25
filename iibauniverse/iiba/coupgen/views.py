from asyncore import write
import code
from urllib import request
from django.forms import NumberInput
from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from .models import Coupon_gener, coupon
from datetime import datetime
from datetime import date
import datetime




def generatecoupon(request):
    if request.method =="POST":
      
        for j in range(0,50):
            code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            coupon_code = ''
            for i in range(0, 7):
                slice_start = random.randint(0, len(code_chars) - 1)
                coupon_code += code_chars[slice_start: slice_start + 1]
            print(coupon_code)
            coupon_ge =Coupon_gener(code= coupon_code)
            coupon_ge.save()

    return render(request,'coupgen/generate.html')


def couponVal(request):
    listOfCoupons =['pawan','kumar','abc']
    getAllCoupon =Coupon_gener.objects.all()
    for item in getAllCoupon:
        insideCoup = item
     
        listOfCoupons.append(str(insideCoup))
    checkBool =2
    if request.method =="POST":
        getAllCoupon = coupon.objects.all()
        coup = request.POST['coup']
        todayDate = date.today()
        expiryDate = datetime.datetime(todayDate.year, todayDate.month+6, todayDate.day)
        if coup not in listOfCoupons:
            return HttpResponse("This is not valid coupon")
        if coup in listOfCoupons:
            if coupon.objects.filter(code=coup).exists():
                return HttpResponse("This is already in use")
        
            couponCheck =coupon(code=request.POST['coup'],expire_date=expiryDate)
            couponCheck.save()
            
            getIDc = couponCheck.id
            return redirect(f"""{getIDc}/checkingCouponStatus""",{id:'getIDc'})
    return render(request,'coupgen/couponVal.html')



def checkingCouponStatus(request,id):
    getstatus=coupon.objects.get(id=id)
    leftdays =getstatus.expire_date- getstatus.publish_date
    print(leftdays)
    return render (request, 'coupgen/checkingCouponStatus.html',{'getStatus':getstatus,'leftDays':leftdays})

# Create your views here.
