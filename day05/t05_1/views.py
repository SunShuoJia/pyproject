from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def register_api(req):
    if req.method == 'GET':
        return render(req,'user/register.html')
    else :
        #获取post请求
        param = req.POST
        u_name = param.get('u_name')
        pwd = param.get('pwd')
        c_pwd = param.get('confirm_pwd')
        #校验用户名
        if len(u_name)>=3:
            if User.objects.filter(username=u_name).exists():
                return HttpResponse('用户已存在')
            else:
                if pwd and len(pwd)>3 and pwd==c_pwd:
                    User.objects.create_user(
                        username=u_name,
                        password=pwd
                    )
                    # return redirect(reversed('t05_1:login'))
                    return HttpResponse('ok')
                else :
                    return HttpResponse('两次密码不一致')
        else :
            return HttpResponse('用户名长度过短')

def login_api(req):
    if req.method == 'GET':
        return render(req,'user/login.html')
    else:
        param = req.POST
        u_name = param.get('uname')
        pwd = param.get('pwd')
        #校验长度
        if pwd and len(pwd)>=3 and u_name and len(u_name)>=3:
            user = authenticate(
                username = u_name,
                password = pwd
            )
            if user:
                # 校验通过，取得用户
                login(req,user)
                return render(req,'index.html',{'u_name':user.username})
            else:
                return render(req,'user/login.html')
        else:
            return HttpResponse("用户名或密码过短")

def logout_api(req):
    logout(req)
    return render(req,'index.html',{'u_name':''})