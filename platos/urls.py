from django.urls import path
from . import views

urlpatterns = [
    path('platos_list/', views.platos_list, name='platos_list'),
    path('platos_orm/', views.platos_orm, name='platos_orm'),

    path('platos_drf_def/', views.platos_precio, name= 'platos_drf_def')

    ]