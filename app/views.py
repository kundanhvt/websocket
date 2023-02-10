from django.shortcuts import render
from .models import Chat, Group

# Create your views here.
def index(request, group_name):
    group, res = Group.objects.get_or_create(name=group_name) 
    chats = group.all_chat.all()
    return render(request,'app/index.html',{"groupname":group_name,"chats":chats})