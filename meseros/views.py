from django.shortcuts import render

from meseros.models import Meseros

from django.db.models import Q
from django.db.models import F

def meseros_list(request):

    data_context = Meseros.objects.all()
    print(data_context)

    return render(request, 'meseros_list.html', context={'data': data_context})


def meseros_orm(request):
    data_context = []

    #meseros = Meseros(nombre='Guillermo', edad=29, procedencia='Perú')
    #meseros.save()

    # query = Q(procedencia='Perú')
    # data_context = Meseros.objects.filter(query, edad__lt=30)

    Meseros.objects.filter().update(edad=F('edad')+5)
    data_context = Meseros.objects.all()




    return render(request, 'meseros_orm.html', context={'data': data_context})