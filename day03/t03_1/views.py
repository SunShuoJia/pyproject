from django.shortcuts import render
from .models import language
# Create your views here.
def Serach(req):
    Input = req.GET
    key = Input.get('key')
    result = language.objects.filter(name__contains=key)
    return render(req,'Serach.html',{'data':result,'title':'方言搜索'})
def Test(req):
    return render(req,'Test.html',context={})