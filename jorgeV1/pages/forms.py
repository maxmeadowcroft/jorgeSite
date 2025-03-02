# pages/forms.py

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name", widget=forms.TextInput(attrs={
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email'
    }))
    phone = forms.CharField(max_length=20, label="Phone", required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Your Phone Number'
    }))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={
        'placeholder': 'Your Message',
        'rows': 5,
    }))
