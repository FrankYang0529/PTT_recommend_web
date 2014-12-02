from django.conf.urls import patterns, url
from recommend import views

urlpatterns = patterns('',
    url(r'^article/$', views.recommend_article, name='recommend_article'),
    url(r'^relation/(?<user_name>\S+)/$', views.relationship, name='relationship'),
)
