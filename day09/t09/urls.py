from django.conf.urls import url
from .views import *

urlpatterns = [
    url (r'^index$', index),
    url (r'^celery$', celery_test)
]
