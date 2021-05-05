from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def people(request):
    # {} if I need to send any content
    return render(request, 'peoplelist.html', {})


def contact(request):
    context = {
        'contact_text': 'Welcome to Contact page',
    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        'about_text': 'Welcome to About page',
    }
    return render(request, 'about.html', context)
