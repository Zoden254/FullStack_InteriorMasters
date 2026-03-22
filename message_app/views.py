from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from e_com.models import User
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Min, Max, Q

# Create your views here.
def messages(request):
    user = request.user
    receivers = ChatHistory.objects.filter(sender=user.username).values_list('receiver__username', flat=True).distinct()
    my_history = ChatHistory.objects.filter(sender=user.username)
    receivers = list(receivers)
    
    recent_chats = my_history

    recent_chats = recent_chats.values('receiver__username', 'receiver__user_number').annotate(messages=Count('receiver__username'), timer=Max('time')).order_by('-timer')

    return render(request, 'messages.html', {'recent_chats': recent_chats})

@login_required(login_url='/login/')
def find_user(request):
    user = request.user
    receiver = ""
    
    if request.GET.get('receiver_no'):
        receiver_number = request.GET.get('receiver_no')
        try:
            receiver = User.objects.get(user_number=str(receiver_number))
            chat_history = ChatHistory.objects.filter(sender=request.user.username, receiver=receiver) | ChatHistory.objects.filter(sender=receiver.username, receiver=request.user)
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

    chat_history = ChatHistory.objects.filter(sender=request.user.username, receiver=receiver).order_by('-time') | ChatHistory.objects.filter(sender=receiver.username, receiver=request.user).order_by('-time')
    
    return render(request, 'chat.html', {'receiver': receiver, 'chats': chat_history})
    
def chat(request, user_number):
    receiver = User.objects.get(user_number=user_number)
    if request.method == "POST":
        message = request.POST.get('message_content')
        if message:
            sent = MessageSent(sender=request.user, receiver_number=user_number, message_content=message)
            sent.save()
            received = MessageReceived(message=sent, receiver=receiver)
            received.save()
            message_id = str(request.user.user_number) + str(receiver.user_number)
            chat_history = ChatHistory(message_content=message,
                                       message_id=message_id,
                                       sender=request.user.username,
                                       receiver=receiver)
                                       
            chat_history.save()
            sent.delete()
            received.delete()
    return HttpResponseRedirect(reverse('message_app:sent', args=(user_number,)))

