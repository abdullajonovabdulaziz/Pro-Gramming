from django.shortcuts import render
from .models import Card,Video,Theme

def home(request):
    cards=Card.objects.all()
    context={'cards':cards}
    return render(request, 'home.html', context)

def lesson(request,title):
    card=Card.objects.get(title=title)
    return render(request, 'lesson.html',{ 'card':card})

def account_def(request):
    return render(request, 'account.html')