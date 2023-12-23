from django.urls import path
from . import views

urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_orm/', views.meseros_orm, name='meseros_orm'),

    ]