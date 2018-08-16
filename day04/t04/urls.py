from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^Myas$',my_as,name='w1'),
    url(r'^serach$',my_serach,name='test'),
    url(r'^index$',index,name='myindex')
]