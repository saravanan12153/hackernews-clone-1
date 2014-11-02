from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime
from urlparse import urlparse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250,)
    url = models.URLField()
    poster = models.ForeignKey(User)
    slug = models.SlugField(max_length=250, unique = True)
    points = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    
    @property
    def domain(self):
	dm = urlparse(self.url).netloc
	if dm.startswith('www.'):
	    dm = dm[4:]

	return dm

    def save(self):
	#super(Post, self).save()
	date = datetime.date.today()
	self.slug = "%i/%i/%i/%s" % (
	    date.year, date.month, date.day, slugify(self.title)
	)

	super(Post, self).save()
	 
    def __unicode__(self):
        return self.title
