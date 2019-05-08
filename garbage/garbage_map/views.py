# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from garbage_map.models import Dot
from garbage_map.models import Category


def index(request, cat=None):
    context = {'dots': Dot.objects.all(), 'categories': Category.objects.all()}
    
    return render(request, 'garbage_map/index.html', context)
