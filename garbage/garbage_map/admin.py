from django.contrib import admin
from garbage_map.models import Dot
from garbage_map.models import Category
from .forms import DotForm


class PersonAdmin(admin.ModelAdmin):
    form = DotForm
    change_form_template = 'admin/app/model/change_form_dot.html'

class CategoryAdmin(admin.ModelAdmin):
    change_form_template = 'admin/app/model/sort_category.html'
    

admin.site.register(Dot, PersonAdmin)
admin.site.register(Category, CategoryAdmin)