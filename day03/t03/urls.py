from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r"^get_player_v1$",get_player_avg_age),
    url(r"^teams$",get_teams),
    url(r"^players$",get_players_by_tid),
    url(r"^getcard$",get_idcard_by_person),
    url(r"^getperson$",get_person_by_card),
    url(r"^delperson$",delete_person),
    url(r"^delcard$",delete_card),
    url(r"^getplayers$",get_player_by_team),
    url(r"^getauthor$",get_author_by_book),
    url(r"^getbook$",get_book_by_author),
]