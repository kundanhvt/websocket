from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=50)
    

class Chat(models.Model):
    chat = models.CharField(max_length=100, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE,related_name="all_chat")