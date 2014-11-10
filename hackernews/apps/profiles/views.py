from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required

from .models import UserProfile

#class ProfileView(DetailView):
   # class Meta:
    #model = UserProfile
    #template_name = "profiles/profile_detail.html" 

#class

#class ProfileUpdate(UpdateView):
    #pass

@login_required    
def profile_view(request):
    profile = request.user.profile
    template_name='profiles/profile_detail.html'
    return render(request, template_name, {
        'profile': profile,
    })
