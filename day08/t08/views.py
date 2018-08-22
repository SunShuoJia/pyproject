import time
from .util import *
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail, send_mass_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.cache import cache_page
from .models import *

from django.db import connection
# Create your views here.
def index(req):
    return render(req,'RTF.html')

@cache_page(60)
def home(req):
    #模拟查询速度慢
    time.sleep(3)
    return HttpResponse('开始')

def fetch_to_dict(cursor):
    colums = [i[0] for i in cursor.description]
    return [dict(zip(colums,row)) for row in cursor.fetchall()]

def ys_cache(req):
    data = cache.get('data')
    if data:
        return HttpResponse(data)
    else:
        time.sleep(3)
        # 获取数据库连接
        cursor = connection.cursor()
        cursor.execute('SELECT name FROM t08_book')
        # res = cursor.fetchall()
        # print(res)
        res = fetch_to_dict(cursor)
        print(res)
        # 缓存数据
        cache.set('data',res[0].get('name'),20)
        return HttpResponse('ok')


def send_my_email(req):
    email_addr = req.GET.get("addr")
    title = 'python1808offer'
    msg = '恭喜您在千锋占座成功'
    # 发送者
    email_from = settings.DEFAULT_FROM_EMAIL
    # 接受者
    receives = [email_addr]
    send_mail(
        title,
        msg,
        email_from,
        receives,
        fail_silently=False
        #设置False失败会被认为是exception的子类
    )
    data = {
        'code':1,
        'msg':'邮件发送成功，请注意查收',
        'data':[]
    }
    return JsonResponse(data)

def sendmail(req):
    return render(req,'sendemail.html')

def send_email_v2(req):
    addr = req.GET.get("addr")
    # 加载Email
    template = loader.get_template('emtemplate.html')
    # 渲染
    html = template.render({'mail':addr})
    title = 'python1808offer'
    msg = '恭喜您在千锋占座成功'
    # 发送者
    email_from = settings.DEFAULT_FROM_EMAIL
    # 接受者
    receives = [addr]
    send_mail (
        title,
        msg,
        email_from,
        receives,
        html_message=html,
        # 设置False失败会被认为是exception的子类
        fail_silently=False
    )
    data = {
        'code': 1,
        'msg': '邮件发送成功，请注意查收',
        'data': []
    }
    return JsonResponse(data)

def send_many_email(req):
    msg1 = (
        '标题1',
        '消息体1',
        settings.DEFAULT_FROM_EMAIL,
        ['justforjs@qq.com', '18355092908@163.com','846134098@qq.com']
    )
    msg2 = (
        '标题1',
        '消息体1',
        settings.DEFAULT_FROM_EMAIL,
        ['justforjs@qq.com', '18355092908@163.com','846134098@qq.com']
    )
    send_mass_mail((msg1,msg2),fail_silently=False)
    return HttpResponse('本是同根生')

def create_confirm_email(req):
    # 生成验证链接
    addr = req.GET.get('addr')
    code = create_random_str()
    url = 'http://{host}/t08/confirm/{random_str}'.format(
        host = req.get_host(),
        random_str = code
    )
    #  发送邮件
    tmp = loader.get_template('emtemplate.html')
    html = tmp.render({'mail':addr,'url':url})
    title = '会员激活'
    msg = ''
    # 发送者
    email_from = settings.DEFAULT_FROM_EMAIL
    # 接受者
    receives = [addr]
    send_mail(
        title,
        msg,
        email_from,
        receives,
        html_message=html,
        # 设置False失败会被认为是exception的子类
        fail_silently=False,
    )
    cache.set(code,addr,900)
    data = {
        'code': 1,
        'msg': '邮件发送成功，请注意查收',
        'data': []
    }
    return JsonResponse (data)

def confirm_api(req,p1):
    #到缓存取数据
    res = cache.get(p1)
    print(res)
    if res:
        cache
        return HttpResponse("激活成功")
    else:
        return HttpResponse('验证链接无效')