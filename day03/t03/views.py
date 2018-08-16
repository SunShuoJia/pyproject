from django.forms import model_to_dict
from django.shortcuts import render
from .models import *
from django.db.models import Avg, Q
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
def get_player_avg_age(req):
#拿国家队的数据
    players = Player.objects.filter(
        team__name="国家队"
    )
    res = players.aggregate(
        Avg("age")
    )
    return HttpResponse(json.dumps(res))

def get_teams(req):
    #查询所有球队数据
    data = Team.objects.raw("select * from t03_team")
    return render(req,"teams.html",{"teams":data})

def get_players_by_tid(req):
    param = req.GET
    t_id = param.get("tid")
    #找对应team_id对应的数据
    res = Player.objects.filter(team_id=int(t_id))
    return render(req,"players.html",{"players":res})

def get_idcard_by_person(req):
    #取个人数据
    p = Person.objects.all().last()
    #取身份证号
    my_card = p.idcard
    print(my_card)
    return HttpResponse(my_card.num)

def get_person_by_card(req):
    #先获取身份证数据
    card = IdCard.objects.get(pk=1)
    #通过身份证找人
    p = card.person
    print(type(p))
    #对象转字典
    res = model_to_dict(p)
    print(type(res))
    return HttpResponse(json.dumps(res))

def delete_person(req):
    person = Person.objects.all().last()
    person.delete()
    return HttpResponse("ok")

def delete_card(req):
    card = IdCard.objects.all().first()
    card.delete()
    return HttpResponse("ok")

def get_player_by_team(req):
    team = Team.objects.get(pk=1)
    players = team.player_set.all().values("name")
    print(type(players))
    # res = [model_to_dict(i) for i in players]
    # return JsonResponse(players)
    return HttpResponse(players)

def get_author_by_book(req):
    book = Book.objects.get(pk=1)
    print(book.author.all())
    print(dir(book.author))
    return HttpResponse(book.author.all())

def get_book_by_author(req):
    author = Author.objects.get(pk=1)
    res = author.book_set.all()
    print(res)
    return HttpResponse(res)