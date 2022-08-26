from django.urls import path

from . import views

urlpatterns = [
    path('cliente/add', views.CustomerCreate.as_view(), name='adicionar_cliente'),
    path('cliente/', views.CustomerListView.as_view(), name='listar_clientes'),
    path('', views.index, name='index'),
]