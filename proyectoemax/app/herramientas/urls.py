from django.conf.urls import url
from app.herramientas import views
#from app.herramientas.views import herramientasCreateView, herramientasListView, herramientasUpdateView, herramientasDeleteView

urlpatterns = [
    url(r'^eliminarherramienta', views.eliminarherramienta, name='eliminar_herramienta'),
    url(r'^editarherramienta', views.modificarherramienta , name='editar_herramienta'),
    url(r'^crearherramienta', views.crearherramienta , name='nueva_herramienta'),
    url(r'^listarherramienta', views.listarherramienta , name='herramienta_lista'),
    url(r'^detalleherramientas/(?P<pk>\d+)/$', views.detaherramienta , name='detalle_herramienta'),
]
