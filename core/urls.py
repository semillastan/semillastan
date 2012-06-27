from django.conf.urls.defaults import url, patterns, include
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('core.views',
    url(r'^$', 'home', name="home"),
    #url(r'about$', direct_to_template, {'template':"about.html"}),
    #url(r'contact$', direct_to_template, {'template':"contact.html"}),
    url(r'about$', 'about', name="about"),
    url(r'contact$', 'contact', name="contact"),
)
