from django.urls import path, include
from .views import PacienteList, \
    PacienteCreate, \
    PacienteUpdate, \
    RelatPacienteList, \
    paciente_detail, \
    Upload, \
    ConsultaCreate, \
    ConsultaList





urlpatterns = [

    #RECIBO
    path('', PacienteList.as_view(), name='paciente_list'),
    path('relatorio_paciente_list', RelatPacienteList.as_view(), name='relatorio_paciente_list'),
    path('consulta', ConsultaList.as_view(), name='consulta_list'),
    path('add-paciente/', PacienteCreate.as_view(), name='paciente_add'),
    path('add-consulta/', ConsultaCreate.as_view(), name='consulta_add'),
    path('<int:pk>/paciente-detail/', paciente_detail, name='paciente_detail'),
    path('<int:pk>/upload/', Upload.as_view(), name='upload'),
    path('<int:pk>/edit-paciente/', PacienteUpdate.as_view(), name='paciente_edit'),





]
