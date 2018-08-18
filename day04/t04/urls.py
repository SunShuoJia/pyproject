from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^Myas$',my_as,name='w1'),
    url(r'^serach/(?P<hh1>\d+)/(?P<hh2>\d+)$',my_serach,name='test'),
    url(r'^index$',index,name='myindex'),
    url(r'getas/(\d+)/(.*)',get_as_by_id,name='getas'),
    url(r'^home$',home)
]