from django.conf.urls.defaults import *
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.auth.views import logout

from views import home, login_user

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login_user, name='login'),
    url(r'^logout/', logout, {'next_page': '/'}, name='logout'),
)
