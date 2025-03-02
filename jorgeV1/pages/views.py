# pages/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")

def services(request):
    return HttpResponse("<h1>Services</h1>")

def contact(request):
    return HttpResponse("<h1>Contact</h1>")

def work_done(request):
    return HttpResponse("<h1>Work Done</h1>")
