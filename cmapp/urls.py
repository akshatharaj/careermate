from django.conf.urls.defaults import *
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.auth.views import logout

from views import home, login_user, add_new_post, list_posts, report_post

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^post/add/$', add_new_post, name='add_post'),
    url(r'^post/$', list_posts, name='list_posts'),
    url(r'^report-post/(?P<post_id>\d+)$', report_post, name='report-post'),
)
