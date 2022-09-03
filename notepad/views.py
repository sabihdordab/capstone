from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse

def index(request):
    if request.user.is_authenticated :
        return render(request,'notepad/index.html')
    else:
        return HttpResponseRedirect(reverse('login'))

def add_note(request):
    if request.method == "POST":
        pass
    else:
        HttpResponse(status=405)