from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import people
def get_datas(req):
    temp = people.objects.all()
    return render(req,"myindex.html",context={"mydata":temp})