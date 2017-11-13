from django.conf.urls import url
from app.proyectos import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    url(r'^eliminarproyecto/(?P<pk>\d+)/$', login_required(views.ProyectoDelete.as_view()), name='ProyectoDelete'),
    url(r'^editarproyecto/(?P<pk>\d+)/$', login_required(views.ProyectoUpdate.as_view()) , name='ProyectoUpdate'),
    url(r'^listarproyecto', login_required(views.ProyectoList.as_view()) , name='ProyectoList'),
    url(r'^crearproyecto', login_required(views.ProyectoCreate.as_view()) , name='ProyectoCreate'),
    url(r'^detalleproyecto/(?P<pk>\d+)/$', login_required(views.ProyectoDetail.as_view()) , name='ProyectoDetail'),
]
