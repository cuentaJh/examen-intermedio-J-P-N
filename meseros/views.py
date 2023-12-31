from django.shortcuts import render
from meseros.models import Meseros

from django.db.models import Q
from django.db.models import F

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from meseros.serializers import MeserosSerializer
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from meseros.forms import MeserosForm
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

    #Meseros.objects.filter().update(edad=F('edad')+5)
    #data_context = Meseros.objects.all()

    return render(request, 'meseros_orm.html', context={'data': data_context})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def meseros(request):
    if request.method == 'GET':
        #queryset = Meseros.objects.filter(edad__gt=25)
        queryset = Meseros.objects.all()
        serializers_class = MeserosSerializer(queryset, many= True)

        return Response(serializers_class.data)

def meseros_create(request):
    form = MeserosForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('meseros_list')
    else:
        form = MeserosForm()
    return render(request, 'meseros_create.html', context={'data':form})

class MeserosList(ListView):
    model = Meseros
    template_name = 'meseros_list_vc.html'


class MeserosCreate(CreateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros_create.html'
    success_url = reverse_lazy('meseros_list_vc')

@api_view(['GET'])
def meseros_peru(request):
    if request.method == 'GET':
        queryset = Meseros.objects.filter(procedencia='Perú')
        serializers_class = MeserosSerializer(queryset, many= True)

        return Response(serializers_class.data)



class MeserosUpdate(UpdateView):
    model = Meseros
    form_class = MeserosForm
    template_name = 'meseros_update_vc.html'
    success_url = reverse_lazy('meseros_list_vc')

class MeserosDelete(DeleteView):
    model = Meseros
    #form_class = MeserosForm
    template_name = 'meseros_confirm_delete.html'
    success_url = reverse_lazy('meseros_list_vc')



@api_view(['POST'])
def meseros_api_view(request):
    if request.method == 'POST':
        print('Data: {}'.format(request.data))
        serializers_class = MeserosSerializer(data=request.data)
        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data)
        return Response(serializers_class.errors)

@api_view(['GET','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def meseros_detail_view(request, pk):
    mesero = Meseros.objects.filter(id=pk).first()

    if mesero:
        if request.method == 'GET':
            serializers_class = MeserosSerializer(mesero)
            return Response(serializers_class.data)

        elif request.method == 'DELETE':
            print('Eliminado correctamente')
            mesero.delete()
            return Response('Mesero eliminado correctamente')

        elif request.method == 'PUT':
            serializers_class = MeserosSerializer(mesero, data=request.data)
            if serializers_class.is_valid():
                serializers_class.save()
                return Response(serializers_class.data)
            return Response(serializers_class.errors)



