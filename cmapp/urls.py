from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin

from views import home

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^admin/', include(admin.site.urls)),
)
