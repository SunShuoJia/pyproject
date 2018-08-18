from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .models import *
# Create your views here.
def my_as(req):
    my_data = MyAs.objects.all()
    # return render(req,"MyAs.html",{"ass":my_data})
    tmp = loader.get_template("MyAs.html")
    print(tmp)
    my_str = tmp.render({'ass':my_data})
    print(my_str)
    my_code = '<h2>hehe</h2>'
    my_code1 = '<script>alert("ok")</script>'
    test = loader.render_to_string('MyAs.html',{'ass':my_data,'code':''})
    print(test)
    return HttpResponse(test)

def my_serach(req,hh1,hh2):
    print(hh1,hh2)
    kw = req.GET.get('kw','')
    data = MyAs.objects.filter(Q(name__contains=kw)|Q(ac__name__contains=kw))
    return render(req,'Serach.html',{'ass':data})

def index(req):
    # 有参数名的反向解析
    # return HttpResponseRedirect(reverse("py1808:getas",kwargs={'hh1':12,'hh2':12}))
    return HttpResponseRedirect(reverse("py1808:getas",args=(3,'lala')))

def get_as_by_id(req,a_id,extra):
    #获取id
    a_id=int(a_id)
    #根据id拿信息
    my_as = MyAs.objects.get(id=a_id)
    #返回给前端
    return HttpResponse(my_as.name+extra)

def home(req):
    return render(req,'work.html')