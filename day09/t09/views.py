import time
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .tasks import test
import logging

logger = logging.getLogger("t09")

# Create your views here.
def index(req):
    logger.info("呵呵")
    a/6
    return HttpResponse("ok")


def celery_test(req):
    n = req.GET.get("n")
    # print("睡前工资10000")
    # time.sleep(int(n))
    # print("睡后1000")
    test.delay(int(n))
    return HttpResponse("好惨")


# @csrf_exempt
@csrf_protect
def zp(req):
    if req.method == "GET":
        return render(req, "zhipiao.html")
    else:
        print(req.POST)
        return HttpResponse("ok")