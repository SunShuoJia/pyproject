from django.conf.urls import url
from .views import Serach,Test
urlpatterns = [
    url(r'^Serach$',Serach),
    url(r'^Test$',Test)
]