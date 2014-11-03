from django.conf.urls import patterns, include, url
from .views import TopScorePostListView

from voting.views import vote_on_object
from .views import PostCreate, PostUpdate, PostDelete
urlpatterns = patterns(
    '',
    url(r'add/$', PostCreate.as_view(), name="post_create"),
    url(r'(P?<pk>[0-9]+)/$', PostUpdate.as_view(), name="post_update"),    
    url(r'(P?<pk>[0-9]+)/delete/$', PostDelete.as_view(), name="post_delete"),
    
    #url(r'(?P<object_id>\d+)/(?P<direction>up|down)vote/?$',
     #vote_on_object, dict(model=Post, template_object_name='link',
			  #template_name='kb/link_confirm_vote.html',
			  #allow_xmlhttprequest=True)),

    #url(r'^(?P[-\w]+)/(?Pup|down)vote/?$', vote_on_object, tip_dict, name="post-voting"),

)
