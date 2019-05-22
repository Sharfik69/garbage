# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from garbage_map.models import Dot
from garbage_map.models import Category
from django.core import serializers
import json

def get_cat(request):
    if request.GET['show'] == '1':
        categories = []
        for cat in Category.objects.order_by('order'):
            cat_item = {
                'id': cat.id,
                'name': cat.name,
                'image': '',
            }
            if cat.image:
                cat_item['image'] = cat.image.url
            categories.append(cat_item)
        return HttpResponse(json.dumps(list(categories)))
    elif request.GET['show'] == '2':
        new_order = request.GET['new_order']
        new_order = json.loads(new_order)
        for i in range(len(new_order)):
            new_rec = Category.objects.get(id=new_order[i]['id_cat'])
            new_rec.order = int(new_order[i]['new_id'])
            new_rec.save()
    return HttpResponse('hello world')
