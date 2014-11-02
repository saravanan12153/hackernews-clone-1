from django.shortcuts import render
from django.utils.timezone import utc
import datetime

from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse

from .models import Post
from .forms import PostForm
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
	
###################### FORMS  ########################
class PostCreate(CreateView, LoginRequiredMixin):
    form_class = PostForm
    template_name = 'posts/forms/create_form.html'

    def get_success_url(self):
        return reverse('index')

	
    def form_valid(self, form):
	#form.instance.Poster = self.request.user
        form.save()
        return super(PostCreate, self).form_valid(form)

    #model = Post
    
class PostUpdate(UpdateView, LoginRequiredMixin):
    form_class = PostForm
    #model = Post   
    template_name = 'posts/forms/update_form.html'

class PostDelete(DeleteView, LoginRequiredMixin):
    # form_class = PostForm
    model = Post
    # success_url = reverse_lazy('???')
 
 
