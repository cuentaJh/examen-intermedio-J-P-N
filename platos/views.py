from django.shortcuts import render

from platos.models import Platos

from django.db.models import Q


def platos_list(request):

    data_context = Platos.objects.all()
    print(data_context)

    return render(request, 'platos_list.html', context={'data': data_context})


def platos_orm(request):
    data_context = []

    # platos = Platos(nombre='Pachamanca', precio=50, procedencia='Perú')
    # platos.save()



    query = Q(procedencia='Perú')
    data_context = Platos.objects.filter(query, precio__gt=40)

    return render(request, 'platos_orm.html', context={'data': data_context})
