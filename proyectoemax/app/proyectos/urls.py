from django.conf.urls import url
from app.proyectos import views

urlpatterns = [
    url(r'^eliminarproyecto/(?P<pk>\d+)/$', views.ProyectoDelete.as_view() , name='ProyectoDelete'),
    url(r'^editarproyecto/(?P<pk>\d+)/$', views.ProyectoUpdate.as_view() , name='ProyectoUpdate'),
    url(r'^listarproyecto', views.ProyectoList.as_view() , name='ProyectoList'),
    url(r'^crearproyecto', views.ProyectoCreate.as_view() , name='ProyectoCreate'),
    url(r'^detalleproyecto/(?P<pk>\d+)/$', views.ProyectoDetail.as_view() , name='ProyectoDetail'),
]
