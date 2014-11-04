from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    #fields = ('title','url')
    list_display =  ('title','url', 'slug', 'points', 'total_votes', 'scores', 'poster', 'created', 'updated')
    search_fields = ('title', 'poster__username', 'poster__first_name', 'poster__last_name')

    fieldsets = [	
	('Post', {
	    'fields': ('title', 'url',  'points', 'total_votes',)
	}),
	
	('Poster', {
	    'fields': ('poster',),
	}),
	
    ]

admin.site.register(Post,PostAdmin)
