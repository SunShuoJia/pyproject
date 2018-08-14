from django.shortcuts import render
from .models import People
# Create your views here.
def get_imformations(req):
    # 查找所有数据
    # temp = People.objects.all()
    # 修改数据
    # People.objects.filter (id=2).update (age=27)
    # 排序
    temp = People.objects.all ().order_by ('-age')
    return render(req,"imformations.html",{'data':temp})
def condition_search(req):
    prarm = req.GET
    keyword = prarm.get("kw")
    # 开头匹配
    # temp = People.objects.filter(name__startswith=keyword)
    # 包含
    # temp = People.objects.filter(name__contains=keyword)
    # 范围
    temp = People.objects.filter(age__range=[20,30])
    return render (req, "imformations.html", {'data': temp})