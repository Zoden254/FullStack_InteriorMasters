from django.db import models
from e_com.models import User
# Create your models here.

class MessageSent(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver_number = models.CharField(max_length=10)
    message_content = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message_content}"
    
class MessageReceived(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(MessageSent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.receiver}'s Message"
    

class ChatHistory(models.Model):
    receiver = models.ForeignKey(User, models.CASCADE)
    message_content = models.CharField(max_length=500)
    message_id = models.CharField(max_length=25, default=0)
    sender = models.CharField(max_length=50)
    #receiver = models.CharField(max_length=50)
    
    time = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return "history"