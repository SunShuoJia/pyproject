from django.conf.urls import url
from .views import get_imformations,condition_search


urlpatterns = [
    url(r'^search$',get_imformations),
    url(r'^condition',condition_search)
]