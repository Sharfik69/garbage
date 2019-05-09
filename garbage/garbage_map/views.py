# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from garbage_map.models import Dot
from garbage_map.models import Category
from django.core import serializers
import json


def index(request, cat=None):
    dots_json = serializers.serialize('json', Dot.objects.all())
    categories_json = serializers.serialize('json', Category.objects.all())
    print(dots_json)
    context = {'dots_json': dots_json, 'categories_json': categories_json, 'categories': Category.objects.all()}
    
    return render(request, 'garbage_map/index.html', context)
