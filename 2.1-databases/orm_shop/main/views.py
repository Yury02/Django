from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale


def cars_list_view(request):
    q = request.GET.get('q')
    template_name = 'main/list.html'
    if q is None:
        cars = Car.objects.all()
        return render(request, template_name, {'cars': cars})  # передайте необходимый контекст
    else:
        cars = Car.objects.filter(model__contains=q)
        # for i in f_cars:
        #     cars = i
        return render(request, template_name, {'cars': cars})  # передайте необходимый контекст


def car_details_view(request, car_id):
    try:
        car_get = Car.objects.get(id=car_id)
        print(car_get)
        car_t = Car.objects.filter(id=car_id)
        for i in car_t:
            car = i
        template_name = 'main/details.html'
        return render(request, template_name, {'car': car})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')


def sales_by_car(request, car_id):
    global car
    try:
        # получите авто и его продажи
        car_t = Car.objects.filter(id=car_id)
        for i in car_t:
            car = i
        sales_t = Sale.objects.filter(car=car_id)
        template_name = 'main/sales.html'
        return render(request, template_name, {'car': car, 'sales': sales_t})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
