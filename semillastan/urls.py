from django.conf import settings
from django.conf.urls.defaults import url, patterns, include
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    #url(r'^projects/', include('projects.urls')),
    #url(r'^bunutan/', include('bunutan.urls', namespace="bunutan")),
    #url(r'^upacm/', include('upacm.urls', namespace="upacm")),
    #url(r'^redefinethejuan/', include('eunice.urls', namespace="eunice")),
    url(r'', include('social_auth.urls')),
    url(r'^', include('core.urls')),
    
    url(r'^joomla$', direct_to_template, {'template':'joomla/home.html'}),
    url(r'^joomla/home$', direct_to_template, {'template':'joomla/home.html'}),
    url(r'^joomla/derverein$', direct_to_template, {'template':'joomla/derverein.html'}),
    url(r'^joomla/archiv$', direct_to_template, {'template':'joomla/archiv.html'}),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
