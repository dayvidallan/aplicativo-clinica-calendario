from django.urls import path, include
from .views import ReciboList, \
    ReciboCreate, \
    ReciboUpdate, \
    recibo_detail, \
    RelatorioList




urlpatterns = [

    #RECIBO
    path('', ReciboList.as_view(), name='financeiro_list'),
    path('relatorio/', RelatorioList.as_view(), name='relatorio_list'),
    path('add-recibo/', ReciboCreate.as_view(), name='recibo_add'),
    path('<int:pk>/detail/', recibo_detail, name='recibo_detail'),
    path('<int:pk>/edit-recibo/', ReciboUpdate.as_view(), name='recibo_edit'),

    #PROCEDIMENTO







]
