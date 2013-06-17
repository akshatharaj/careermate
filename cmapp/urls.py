from django.conf.urls.defaults import *
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.auth.views import logout

from views import (home, login_user, add_new_post, list_posts, report_post, 
respond_to_post, post_detail)

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^new-post/$', add_new_post, name='new_post'),
    url(r'^new-post/add$', add_new_post, name='add_new_post'),
    url(r'^post/$', list_posts, name='list_posts'),
    url(r'^post/(?P<post_id>\d+)$', post_detail, name='post-detail'),
    url(r'^report-post/(?P<post_id>\d+)$', report_post, name='report-post'),
    url(r'^report-post/add$', report_post, name='new-report-post'),
    url(r'^respond-to-post/(?P<post_id>\d+)$', respond_to_post, name='respond-to-post'),
    url(r'^respond-to-post/add$', respond_to_post, name='new-response'),
)
