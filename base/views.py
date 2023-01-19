from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 1, 'name': 'Design with me !'},
    {'id': 1, 'name': 'Frontend Devs!'},
]


def home(request):
    return render(request, 'home.html')


def room(request):
    return render(request, 'room.html')
