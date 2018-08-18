from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^register$',register_api,name='register'),
    url(r'^login$',login_api,name='login'),
    url(r'^logout$',logout_api,name='logout')
]