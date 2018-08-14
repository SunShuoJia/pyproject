from django.conf.urls import url,include
from django.contrib import admin
from .views import my_carts,search_by_name


urlpatterns=[
    url(r"^trains$",my_carts),
    url(r"^getcart$",search_by_name)
]