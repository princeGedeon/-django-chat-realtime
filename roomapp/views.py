from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from roomapp.models import Room, Message


def home(request):
    return render(request,'index.html')

@login_required
def rooms(request):
    rooms=Room.objects.all()

    return render(request,'room/rooms.html',context={'rooms':rooms})

@login_required
def room(request,slug):
    room=Room.objects.get(slug=slug)
    messages=Message.objects.filter(room=room)[0:30]


    return  render(request,'room/room.html',context={"room":room,"messages":messages})