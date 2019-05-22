# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from garbage_map.models import Dot
from garbage_map.models import Category
from django.core import serializers
import json


def get_cat(request):
    """
    Отдает категории для списка сортировки
    """
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
    return HttpResponse(json.dumps(categories), content_type="application/json")


def save_order(request):
    """
    Сохраняет порядок сортировки
    """
    new_order = request.GET['new_order']
    new_order = json.loads(new_order)

    for item in new_order:
        cat = Category.objects.get(id=item['id'])
        cat.order = int(item['order'])
        cat.save()

    return HttpResponse('ok')
