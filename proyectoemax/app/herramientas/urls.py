from django.conf.urls import url
from app.herramientas import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
#from app.herramientas.views import HerramientaCreate, HerramientaList,
urlpatterns = [
    url(r'^eliminarherramienta/(?P<pk>\d+)/$', login_required(views.HerramientaDelete.as_view()) , name='HerramientaDelete'),
    url(r'^editarherramienta/(?P<pk>\d+)/$', login_required(views.HerramientaUpdate.as_view()) , name='HerramientaUpdate'),
    url(r'^listarherramienta', login_required(views.HerramientaList.as_view()) , name='HerramientaList'),
    url(r'^crearherramienta', login_required(views.HerramientaCreate.as_view()) , name='HerramientaCreate'),
    url(r'^detalleherramientas/(?P<pk>\d+)/$', login_required(views.HerramientaDetail.as_view()) , name='HerramientaDetail'),
    url(r'^reporteherramientas', views.reporte , name='reporte'),
]
