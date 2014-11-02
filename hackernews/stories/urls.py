from django.conf.urls import patterns, include, url
from stories.views import TopScorePostListView

urlpatterns = patterns(
    '',
    url(r'^$', TopScorePostListView.as_view()),
    #url(r'^$', include('stories.urls')),

)
