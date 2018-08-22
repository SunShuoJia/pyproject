import uuid

import hashlib
import os
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_login(req):
    if req.method=='GET':
        return render(req,'login.html')
    else:
        #处理登陆逻辑
        param = req.POST
        uname = param.get('uname')
        pwd = param.get('pwd')
        #验证用户
        user = authenticate(username=uname,password=pwd)
        if user:
            login(req,user)
            return HttpResponse('ok')
        else:
            return HttpResponse('账号或密码错误')
@login_required(login_url = '/t06/login')
def get_login_user(req):
    user = req.user
    return HttpResponse('欢迎{u_name}'.format(u_name = user.username))

@login_required(login_url = '/t06/login')
def upload_img_v1(req):
    if req.method=='GET':
        u_name = req.user.username
        tmp = req.user.icon
        icon = tmp.url if tmp else ""
        #获取域名
        host = req.get_host()
        print(host)
        icon_str = 'http://'+host+'/static/imgs/'+icon
        print(icon_str)
        return render(req,'uploadimg.html',{'uname':u_name,'u_icon':icon_str})
    else:
        #拿文件
        my_img = req.FILES.get('img')
        #确定上传者
        user = req.user
        #保存数据到对应数据库字段中
        user.icon = my_img
        #保存修改
        user.save()
        return HttpResponse("ok")

def get_unique_name():
    #获得一个UUID
    uuid_val = uuid.uuid4()
    #将uuid转成字符串
    uuid_str = str(uuid_val).encode('utf-8')
    #获得一个MD5
    md5 = hashlib.md5()
    #将uuid字符串做摘要
    md5.update(uuid_str)
    #返回32位16进制结果
    return md5.hexdigest()


def upload_img_v2(req):
    if req.method =='POST':
        img = req.FILES.get('img')
        file_name = get_unique_name()+'.png'
        file_path = os.path.join(settings.MEDIA_ROOT,file_name)
        with open(file_path,'wb') as fp:
            for i in img.chunks():
                fp.write(i)
        print(file_path)
        return HttpResponse('ok')