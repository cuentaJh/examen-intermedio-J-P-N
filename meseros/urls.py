from django.urls import path
from . import views

urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_orm/', views.meseros_orm, name='meseros_orm'),

    path('meseros_drf_def/', views.meseros, name= 'meseros_drf_def'),
    path('meseros_create/', views.meseros_create, name='meseros_create'),

    path('meseros_list_vc/', views.MeserosList.as_view(), name='meseros_list_vc'),
    path('meseros_create_vc/', views.MeserosCreate.as_view(), name='meseros_create_vc'),
    path('meseros_edit_vc/<int:pk>', views.MeserosUpdate.as_view(), name='meseros_edit_vc'),
    path('meseros_delete_vc/<int:pk>', views.MeserosDelete.as_view(), name='meseros_delete_vc'),

    path('meseros_drf_peru/', views.meseros_peru, name='meseros_drf_peru'),
    path('meseros_list_drf_def/', views.meseros_api_view, name='owner_list_drf_def'),
    path('meseros_detail_drf_def/<int:pk>', views.meseros_detail_view, name='owner_detail_drf_def'),
    ]