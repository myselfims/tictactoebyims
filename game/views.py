from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Game
import random

# Create your views here.

def idgenerator():
    code = []
    for i in range(8):
        number = random.randint(1,9)
        code.append(number)
    return code

def home(request,roomcode):
    
    players = Game.objects.filter(room_code = roomcode)
    print(len(players))
    if len(players) > 0:
        return render(request,'hall.html',{'players':players})
    else:
        return redirect('/')
def lobby(request):
    return render(request,'lobby.html')