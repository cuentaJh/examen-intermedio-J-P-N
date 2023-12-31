from django.shortcuts import render

from platos.models import Platos
from django.db.models import F

from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response
from platos.serializers import PlatosSerializer


def platos_list(request):

    data_context = Platos.objects.all()
    print(data_context)

    return render(request, 'platos_list.html', context={'data': data_context})


def platos_orm(request):
    data_context = []

    # platos = Platos(nombre='Pachamanca', precio=50, procedencia='Perú')
    # platos.save()



    #query = Q(procedencia='Perú')
    #data_context = Platos.objects.filter(query, precio__gt=40)

    data_context= Platos.objects.filter(precio__lt=15)
    data_context.delete()

    return render(request, 'platos_orm.html', context={'data': data_context})

@api_view(['GET'])
def platos_precio(request):
    if request.method == 'GET':
        queryset = Platos.objects.filter(precio__gte=50)
        serializers_class = PlatosSerializer(queryset, many= True)

        return Response(serializers_class.data)

