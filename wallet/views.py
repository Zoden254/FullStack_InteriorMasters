from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Wallet
from django.http import HttpResponseRedirect

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
        return redirect('wallet:wallet')
    else:
        return render(request, 'deposit.html')