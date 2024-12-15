from django.shortcuts import render
from .models import Brand,Car

def asosiy(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    contects = {
        'brands' : brands,
        'cars' : cars,
    }
    return render(request, 'index.html', context= contects)

def select(request, brand_id):
    brands = Brand.objects.all()
    cars = Car.objects.filter(course = brand_id)

    contexts = {
        'brands': brands,
        'cars': cars,
    }
    return render(request, "index.html", context = contexts)

def select_car(request, car_id):
    brands = Brand.objects.all()
    cars = Car.objects.filter(car = car_id)
    contexts = {
       'brands' : brands,
        'cars' : cars,
    }
    return render(request, "index.html", context = contexts)
