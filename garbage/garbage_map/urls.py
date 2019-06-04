import re

from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from garbage_map.models import Dot
from . import views, admin_views


urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^admin/categories/$', admin_views.get_cat, name = "get_cat"), 
    url(r'^admin/save_order/$', admin_views.save_order, name = "save_order"), 
]
