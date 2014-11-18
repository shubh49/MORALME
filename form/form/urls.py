from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'form.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^forms/', include('forms.urls', namespace = "forms")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^thanks/', include('forms.urls', namespace = "thanks")),
    url(r'^getd/', include('forms.urls', namespace = "forms")),
)
