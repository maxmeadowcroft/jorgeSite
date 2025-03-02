# pages/views.py

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Project, ProjectImage
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'pages/home.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ServicesView(TemplateView):
    template_name = 'pages/services.html'


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # For debugging, print the values to the console
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)

        # Process the data as needed (e.g., send an email, save to a database, etc.)

        # Redirect to a thank-you page after processing
        return redirect('contact_success')

    return render(request, 'pages/contact.html')


def contact_success_view(request):
    return render(request, 'pages/contact_success.html')

def work_done_view(request):
    projects = Project.objects.all().prefetch_related('images')
    return render(request, 'pages/work_done.html', {'projects': projects})
