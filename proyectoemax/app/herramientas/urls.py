from django.conf.urls import url
from app.herramientas import views
#from app.herramientas.views import HerramientaCreate, HerramientaList,
urlpatterns = [
    url(r'^eliminarherramienta/(?P<pk>\d+)/$', views.HerramientaDelete.as_view() , name='HerramientaDelete'),
    url(r'^editarherramienta/(?P<pk>\d+)/$', views.HerramientaUpdate.as_view() , name='HerramientaUpdate'),
    url(r'^listarherramienta', views.HerramientaList.as_view() , name='HerramientaList'),
    url(r'^crearherramienta', views.HerramientaCreate.as_view() , name='HerramientaCreate'),
    url(r'^detalleherramientas/(?P<pk>\d+)/$', views.HerramientaDetail.as_view() , name='HerramientaDetail'),
]
