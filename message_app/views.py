from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from e_com.models import User
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def messages(request):
    return render(request, 'messages.html')

@login_required(login_url='/login/')
def find_user(request):
    user = request.user
    receiver = ""
    
    if request.GET.get('receiver_no'):
        receiver_number = request.GET.get('receiver_no')
        try:
            receiver = User.objects.get(user_number=str(receiver_number))
            chat_history = ChatHistory.objects.filter(sender=request.user.username, receiver=receiver) | ChatHistory.objects.filter(sender=receiver.username, receiver=request.user.username)
            return render(request, 'chat.html', {'receiver': receiver, 'chats': chat_history})
        except ObjectDoesNotExist:
            return render(request, 'find_user.html', {'error_message' : "Not Found"})
    else:
        return render(request, 'find_user.html')

    
def message_sent(request, user_number):
    receiver = User.objects.get(user_number=user_number)
    sender = request.user
    sender_messages = MessageSent.objects.filter(sender=sender, receiver_number=receiver.user_number)
    receiver_messages = MessageSent.objects.filter(sender=receiver, receiver_number=sender.user_number)

    chat_history = ChatHistory.objects.filter(sender=request.user.username, receiver=receiver) | ChatHistory.objects.filter(sender=receiver.username, receiver=request.user.username)
    
    return render(request, 'chat.html', {'receiver': receiver, 'chats': chat_history})
    
def chat(request, user_number):
    receiver = User.objects.get(user_number=user_number)
    if request.method == "POST":
        message = request.POST['message_content']
        if message:
            sent = MessageSent(sender=request.user, receiver_number=user_number, message_content=message)
            sent.save()
            received = MessageReceived(message=sent, receiver=receiver)
            received.save()
            chat_history = ChatHistory(message_content=message,
                                       sender=request.user.username,
                                       receiver=receiver)
                                       
            chat_history.save()
    return HttpResponseRedirect(reverse('message_app:sent', args=(user_number,)))
