# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from garbage_map.models import Dot
from garbage_map.models import Category
from django.core import serializers
import json


def index(request, cat=None):

    dots = []
    for dot in Dot.objects.all():
        dot_item = {
            'id': dot.id,
            'name': dot.name,
            'description': dot.description,
            'x': dot.x,
            'y': dot.y,
            'working_hours': dot.working_hours,
            'addres': dot.addres,
            'image': dot.image.url,
            'categories': [id[0] for id in dot.categories.values_list('id')],
        }
        dots.append(dot_item)
    categories = []
    for cat in Category.objects.all():
        cat_item = {
            'id': cat.id,
            'name': cat.name,
            'image': '',
        }
        if cat.image:
            cat_item['image'] = cat.image.url
        categories.append(cat_item)
    #categories_json = serializers.serialize('json', Category.objects.all())
    # print(dots_json)
    context = {'dots_json': json.dumps(list(dots)), 'categories_json': json.dumps(list(categories)), 'categories': Category.objects.order_by('order')}
    
    return render(request, 'garbage_map/index.html', context)
