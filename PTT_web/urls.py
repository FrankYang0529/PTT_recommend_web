from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PTT_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('pages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^recommend/', include('recommend.urls')),
)
