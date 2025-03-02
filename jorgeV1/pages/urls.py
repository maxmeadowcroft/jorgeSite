# pages/urls.py
from django.urls import path
from .views import HomeView, AboutView, ServicesView, work_done_view, contact_view, contact_success_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
    path('work-done/', work_done_view, name='work_done'),
]
