from django.shortcuts import render
from django.http import HttpResponse
from .models import FireCart
# Create your views here.
def my_carts(req):
    #拿数据
    data = FireCart.objects.filter(speed__lte=500).order_by("speed")
    #准备返回数据
    result ={
        "title":"火cart",
        "carts":data
    }
    return render(req,"trains.html",result)
def search_by_name(req):
    param = req.GET
    kw = param.get("kw")
    #根据参数，搜索数据
    res = FireCart.objects.filter(
        name__contains=kw
    )
    print(param)
    return render(req,"trains.html",{"carts":res})