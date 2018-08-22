import random
import os
import io
from PIL import Image,ImageDraw,ImageFont
from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from .util import *
# Create your views here.
PAGE_PEER_NUM = 10
def person_api(req,current_page):
    # 获取所有数据
    persons = Person.objects.all()
    datas = []
    #实例化分页对象
    paginator = Paginator(
        persons,
        PAGE_PEER_NUM
    )
    try:
        page = paginator.page(current_page)
        datas = page.object_list
    except:
        pass
    data = {
        'person':datas,
        'page_range':paginator.page_range,
        'page':page,
        'last_page':paginator.num_pages
    }
    return render(req,'paginator.html',data)

def get_confirm_img(req):
    # 选择颜色
    bg = get_random_color()
    # 设置画布大小
    img_size = (150,50)
    # 实例化画布
    image = Image.new('RGB',img_size,bg)
    # 实例化画笔
    draw = ImageDraw.Draw(image)
    # 实例化字体
    font_path = os.path.join(settings.BASE_DIR,'static/fonts/ADOBEARABIC-BOLDITALIC.OTF')
    font_size = 30
    my_font =ImageFont.truetype(font_path,font_size)
    # 绘画
    # font_color = (0,255,0)
    source = 'zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP0123456789'
    loop = 4
    confirm_code = ""
    for i in range(loop):
        tmp = random.randrange(len(source))
        tmp_str = source[tmp]
        confirm_code += tmp_str
        draw.text((20+30*i,10),tmp_str,get_random_color(),font=my_font)
    # 保存
    buf = io.BytesIO()
    # 保存图片到io流中
    image.save(buf,'png')
    #设置session,将生成的四位验证码保存在session中
    req.session['c_code']=confirm_code
    return HttpResponse(buf.getvalue(),content_type='image/png')

def my_login(req):
    return render(req,'login.html')

def confirm_api(req):
    #获取用户传递的参数
    user_code = req.POST.get("code")
    #从session中获取生成的验证码字符
    bg_code = req.session.get("c_code")
    #不区分大小写验证lower
    #根据不同的结果返回数据
    if user_code.lower() == bg_code.lower():
        data = {
            "code": 1,
            "msg": "ok",
            "data": []
        }
        return JsonResponse(data)
    else:
        data = {
            "code": 2,
            "msg": "验证码错误",
            "data": []
        }
        return JsonResponse(data)

