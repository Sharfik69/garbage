from django.shortcuts import render
from django.http import HttpResponse
from garbage_map.models import Dot
from garbage_map.models import Category


def index(request):
    context = {'dots': Dot.objects.all(), 'category': Category.objects.all()}
    
    return render(request, 'map_yandex/index.html', context)