from django.shortcuts import render, redirect
from .models import Video, User
from .forms import VideoForm, UserForm

def videos(request):
    lista = Video.objects.all()
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('videos')
    else:
        form = VideoForm()
    return render(request, "videos.html", {"lista": lista, "form": form})


def users(request):
    lista = User.objects.all()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm()
    return render(request, "users.html", {"lista": lista, "form": form})


def credits(request):
    return render(request, "credits.html")
