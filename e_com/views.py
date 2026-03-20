from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import *
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist

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

    def get_queryset(self):
        return Service.objects.order_by('-id')

def about(request):
    return render(request, 'engage.html')

def login_view(request):
    if request.method == 'POST':
        user_name = request.POST["username"]
        pass_word = request.POST["password"]

        user = authenticate(request, username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next')

            if next_url:
                return redirect(next_url)
            else:
                return redirect('e_com:home')
        else:
            messages.error(request, "User not found")
            return HttpResponseRedirect(reverse('e_com:login'))
    return render(request, 'login.html')
    


@login_required(login_url='/login/')
def comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        if comment != "":
            new_comment = request.user.comment_set.create(comment=comment)
            new_comment.save()
            return HttpResponseRedirect(reverse('e_com:home'))
        else:
            return HttpResponseRedirect(reverse("e_com:engage"))
    else:
        return redirect('e_com:engage')

        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('e_com:home'))

@login_required(login_url='/login/')
def profile_view(request):
    return render(request, 'profile.html')

def signup(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'signup.html')

def create_user_view(request):
    firstname = request.POST['firstname']
    lastname = request.POST['last_name']
    username = request.POST['user_name']
    email = request.POST['email']
    user_number = request.POST['user_number']
    password = request.POST['pass_word']
    password2 = request.POST['confirm_pass_word']

    if request.method == 'POST':
        if password == password2:
            if username not in User.objects.values_list('username', flat=True):
                if email not in User.objects.values_list('email', flat=True):
                    if user_number not in User.objects.values_list('user_number', flat=True):
                        User.objects.create_user(username=username, password=password, email=email, user_number=user_number, first_name=firstname, last_name=lastname)

                    else:
                        messages.error(request, "Phone number already used")
                        return HttpResponseRedirect(reverse('e_com:signup'))

                else:
                    messages.warning(request, "Email already used")
                    return HttpResponseRedirect(reverse('e_com:signup'))
            else:
                messages.warning(request, "Username already exist")
                return HttpResponseRedirect(reverse('e_com:signup'))
        else:
            messages.error(request, "Password Mismatch")
            return HttpResponseRedirect(reverse('e_com:signup'))
        return HttpResponseRedirect(reverse('e_com:login'))
    else:
        return HttpResponseRedirect(reverse('e_com:signup'))
    
#@login_required(login_url='/login/')
def service_view(request, id):
    service = Service.objects.get(id=id)
    if request.user.is_authenticated:
        my_cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        my_cart = {}
    return render(request, 'service_view.html', {'service': service, 'my_cart': my_cart})

@login_required(login_url='/login/')
def add_item_to_cart(request, id):
    user = request.user
    item = Service.objects.get(id=id)
    item_to_cart, created = Cart.objects.get_or_create(user=user)
    item_to_cart.item.add(item)
    
    return HttpResponseRedirect(reverse('e_com:services'))

@login_required(login_url='/login/')
def cart_view(request):
    user = request.user
    
    my_cart, created = Cart.objects.get_or_create(user=user)
    cart_items = my_cart.item.order_by
    
    #Here I extract the service model from the cart model.
    
    #cart_items = user.cart.item.all()

    return render(request, 'cart.html', {'items' : cart_items})


def remove_from_cart(request, name):
    user = request.user
    from_service = Service.objects.get(name=name)
    cart = Cart.objects.get(user=user)
    cart.item.remove(from_service)
    return HttpResponseRedirect(reverse('e_com:cart_view'))

def apply_service(request, service_id):
    service = Service.objects.get(id=service_id)    
    min_deposit = int(service.cost_range) * int(service.minimum_deposite) / 100
    if request.method == 'POST':
        deposit = float(request.POST['deposit'])
        password = request.POST['password']

        if not request.user.check_password(password):
            messages.error(request, f"Wrong Password.")
            return HttpResponseRedirect(reverse('e_com:apply_service', args=(service_id,)))

        if deposit < min_deposit:
            messages.error(request, f"The minimum Deposit for this service is {min_deposit}")
            return HttpResponseRedirect(reverse('e_com:apply_service', args=(service_id,)))

        balance = float(service.cost_range) - deposit
        purchase = ServiceBought(customer=request.user, service=service, deposit=deposit, balance=balance)
        purchase.save()
        transaction_code = f"INT_MA{purchase.id}"
        
        messages.success(request, f"Payment transaction {transaction_code} Success.")
        return redirect('e_com:success')    
        
    return render(request, "apply_service.html", {'service': service, 'min_deposit': min_deposit})

def success_page(request):
    return render(request, "success_purchase.html")

