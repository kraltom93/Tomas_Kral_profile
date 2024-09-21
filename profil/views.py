from django.shortcuts import render

def home(request):
    return render(request, 'profil/home.html')

def contact(request):
    return render(request, 'profil/contact.html')
