from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

#The home Page
def home(request):
    comments = Comment.objects.all()
    context = {
        'comments' : comments,
    }
    return render(request, 'index.html', context)

def SamplesList(request):
    return render(request, "samples.html")

class ServicesList(generic.ListView):
    model = Service
    template_name = 'services.html'
    context_object_name = 'services'

def about(request):
    return render(request, 'engage.html')

def login_view(request):
    return render(request, 'login.html')
    
def authentication(request):
    user_name = request.POST["username"]
    pass_word = request.POST["password"]

    user = authenticate(request, username=user_name, password=pass_word)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('e_com:home'))
    else:
        return render(request, 'login.html', {'error_message' : "User not found"})

@login_required
def comment(request):
    if request.user.is_authenticated:
        comment = request.POST['comment']
        if comment != "":
            new_comment = request.user.comment_set.create(comment=comment)
            new_comment.save()
            return HttpResponseRedirect(reverse('e_com:home'))
        else:
            return HttpResponseRedirect(reverse("e_com:engage"))
    else:
        return HttpResponseRedirect(reverse('e_com:home'))
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('e_com:home'))

@login_required
def profile_view(request):
    return render(request, 'profile.html')


def signup(request):
    return render(request, 'signup.html')

def create_user_view(request):
    return HttpResponseRedirect(reverse('e_com:login'))