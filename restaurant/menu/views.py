from django.shortcuts import render
from .models import Dish

def menu(request):
  dishes = Dish.objects.all()
  return render(request, 'menu/menu.html', {'dishes': dishes})

def contact(request):
  return render(request, 'menu/contact.html')
