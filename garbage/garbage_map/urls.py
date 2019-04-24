import re

from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from garbage_map.models import Dot
from . import views


urlpatterns = [
    url(r'^$', views.index, name = "index")
]