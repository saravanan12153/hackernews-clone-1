from django.conf.urls import patterns, include, url
from .views import TopScorePostListView

from .views import PostCreate, PostUpdate, PostDelete
urlpatterns = patterns(
    '',
    url(r'add/$', PostCreate.as_view(), name="post_create"),
    url(r'(P?<pk>[0-9]+)/$', PostUpdate.as_view(), name="post_update"),
    url(r'(P?<pk>[0-9]+)/delete/$', PostDelete.as_view(), name="post_delete"),    
)
