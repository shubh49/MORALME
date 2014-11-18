from django.conf.urls import patterns , include, url
from django.contrib import admin
from forms import views
urlpatterns = patterns('',
                        url(r'^$', views.getdetails, name = 'signupdetails'),
                        #url(r'^getd/', views.getdetails, name = 'signupdetails'),
                        url(r'^thanks/', views.thanks, name = 'thanks')
                        )