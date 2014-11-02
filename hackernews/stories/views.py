from django.shortcuts import render
from django.utils.timezone import utc
import datetime
from django.views.generic import ListView
from .models import Post

############ TOP SCORE FRONT END ##############

def post_score(post, gravity=1.8, timebase=120):
    points = (post.points - 1)**(gravity-1)
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    age = int((now - post.created).total_seconds())/60
    
    return points/(age+timebase)**gravity


def top_score_posts(top=100, consider=180):
    latest_posts = Post.objects.order_by('-created')[:consider]
    ranked_posts = sorted([ (post_score(post), post) for post in latest_posts ], reverse=True)
    return [ post for (score,post) in ranked_posts ][:top]

class TopScorePostListView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = 'top_ranked_posts'
    def get_queryset(self):
	return top_score_posts()
