from django.db import models
from django.contrib.auth.models import User
from uuslug import slugify
import datetime
from urlparse import urlparse

from .scores import post_score
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250,)
    url = models.URLField()
    poster = models.ForeignKey(User)
    slug = models.SlugField(max_length=250, unique = True)
    # points = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    points = models.IntegerField(default=1)
    total_votes =  models.IntegerField(null=True)
    scores = models.FloatField(null=True)    
    
    @property
    def domain(self):
	dm = urlparse(self.url).netloc
	if dm.startswith('www.'):
	    dm = dm[4:]
	return dm

    @models.permalink
    def get_absolute_url(self):
	return 'post_detail', (), {'slug': self.slug}
	
    def save(self):
	#super(Post, self).save()
	import time
	date = datetime.date.today()
	self.slug = "%i-%i-%i/%s-%i" % (
	    date.year, date.month, date.day, slugify(self.title), time.time()
	)
	#self.points = self.upvotes - self.downvotes
	if self.total_votes is None:
	    self.total_votes = 1
	self.scores = post_score(self)

	super(Post, self).save()
	
	 
    def __unicode__(self):
        return self.title
