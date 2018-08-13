from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Engineer

def index(request):
    return HttpResponse("Django 呵呵哒！！")

def my_html(request):
    return render(request,'my_index.html')

def get_data(req):
    #获取数据
    data = Engineer.objects.all()
    print(data)
    return render(req,"my_index.html",context={"my_data":data})
