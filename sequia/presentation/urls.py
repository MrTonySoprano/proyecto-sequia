from django.urls import path
from django.views.generic import TemplateView
from .views import MedidaList, MedidaCreate, MedidaUpdate, MedidaDelete

urlpatterns = [
    # Home
    path('', TemplateView.as_view(template_name="sequia/home.html"), name='home'),
    
    # Medidas
    path('medidas/', MedidaList.as_view(), name='medida_list'),
    path('medidas/nueva/', MedidaCreate.as_view(), name='medida_create'),
    path('medidas/<int:pk>/editar/', MedidaUpdate.as_view(), name='medida_update'),
    path('medidas/<int:pk>/eliminar/', MedidaDelete.as_view(), name='medida_delete'),
]