from django.contrib import admin
from django import forms
from django.forms import ModelForm
from forms.models import signup
# Register your models here.

class Adminform(admin.ModelAdmin):
     list_display = ('name', 'uname','email','pwd')
     list_filter = ['uname']
     search_fields = ['uname']
     
admin.site.register(signup, Adminform)
