from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Wallet
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.contrib.humanize.templatetags.humanize import intcomma

# Create your views here.



@login_required
def wallet(request):
    wallet, created = Wallet.objects.get_or_create(user=request.user)
    return render(request, 'wallet.html', {'wallet':wallet})

def deposit(request):
    my_wallet, created = Wallet.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        my_wallet.balance += int(amount)
        my_wallet.save()
        messages.success(request, f"Successfully deposited Ksh.{intcomma(amount)}")
        return redirect('wallet:wallet')
    else:
        return render(request, 'deposit.html')


def withdraw(request):
    my_wallet, created = Wallet.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        password = request.POST.get('password')

        if request.user.check_password(password):
            if my_wallet.balance < int(amount):
                messages.error(request, f"Insufficient funds in your account to withdraw Ksh{intcomma(amount)}. Your account balance is Ksh{intcomma(my_wallet.balance)}.")
                return redirect('wallet:wallet')
            else:
                my_wallet.balance -= int(amount)
                my_wallet.save()
                messages.success(request, f"Successfully withdrawn Ksh{intcomma(amount)}")
                return redirect('wallet:wallet')
        else:
            messages.error(request, f"Wrong Password")
            return redirect('wallet:wallet')

    else:
        return render(request, 'withdraw.html')