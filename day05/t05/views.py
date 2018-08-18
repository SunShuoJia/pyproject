from django.shortcuts import render
from .models import *
from django.db.models import Q,F,Aggregate
from django.http import HttpResponse, HttpResponseRedirect, QueryDict, JsonResponse
from django.urls import reverse
from django.template import loader
# Create your views here.
def game(req):
    return render(req,'2048.html')

def testreq(req):
    # print(dir(req))
    # print(req.method)#打印请求方法
    # print(req.POST)#POST请求
    # print(req.COOKIES)# 打印cookie
    # print(req.META.get("REMOTE_ADDR"))#打印用户IP
    # print(req.FILES)
    # param = QueryDict(req.body)
    # print(param)
    # print(req.path)#请求路径
    # print(req.get_host())#拿请求的域名端口
    # print(req.get_port())#访问端口
    # response = HttpResponse()
    # response.content="123"
    # response.status_code = 404
    # response.write("456")
    # response.flush()
    # response.content="789"
    my_dict = {'key':'呵呵'}
    return JsonResponse(my_dict)

# 首页API
def index(req):
    user_name = req.COOKIES.get("uname","")
    data = req.session.get('msg')
    print(data)
    return render(req,'index.html',{'u_name':user_name})

def login_api(req):
    if req.method == 'GET':
        return render(req,'login.html')
    else :
        param = req.POST
        u_name = param.get('uname')
        pwd = param.get('pwd')
        req.session['msg'] = 'ok'
        #用户校验(假设通过)

        response = HttpResponseRedirect('/t05/index')
        print(response)
        # 设置cookie
        response.set_cookie('uname',u_name,max_age=10)
        return response

def logout_api(req):
    response = HttpResponseRedirect(reverse('t05:index'))
    del req.session['msg']
    response.delete_cookie('uname')
    return response