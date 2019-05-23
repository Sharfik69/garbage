# coding=utf-8
from django import forms
from .models import Dot, Category

class DotForm(forms.ModelForm):
    class Meta:
        model = Dot
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'ООО Ромашка'}),
            'addres': forms.TextInput(attrs={'placeholder': 'Адрес'})
        }
class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'name_html', 'image', 'order')
