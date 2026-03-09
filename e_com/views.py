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

class SamplesList(generic.ListView):
    model = Sample
    template_name = 'samples.html'
    context_object_name = 'samples'

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

@login_required(login_url='/login/')
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
        return HttpResponseRedirect(reverse('e_com:login'))

        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('e_com:home'))

@login_required(login_url='/login/')
def profile_view(request):
    return render(request, 'profile.html')


def signup(request):
    return render(request, 'signup.html')

def create_user_view(request):
    username = request.POST['user_name']
    password = request.POST['pass_word']
    password2 = request.POST['confirm_pass_word']
    if password == password2:
        User.objects.create_user(username=username, password=password)


    return HttpResponseRedirect(reverse('e_com:login'))

def service_view(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'service_view.html', {'service': service})

