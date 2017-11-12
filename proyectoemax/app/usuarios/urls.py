from django.conf.urls import url
from app.usuarios import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    url(r'^login/$' , views.authentication , name='authentication'),
    url(r'^logout/$' , auth_views.logout , {'next_page':'/login'}, name='logout'),
    url(r'^listarusuarios/$' , views.UsuarioList.as_view() , name='UsuarioList'),
    url(r'^eliminarusuario/(?P<pk>\d+)/$', views.UsuarioDelete.as_view() , name='UsuarioDelete'),
    url(r'^editarusuario/(?P<pk>\d+)/$', views.UsuarioUpdate.as_view() , name='UsuarioUpdate'),
    url(r'^crearusuario', views.UsuarioCreate.as_view() , name='UsuarioCreate'),
    url(r'^detalleusuario/(?P<pk>\d+)/$', views.UsuarioDetail.as_view() , name='UsuarioDetail'),
]
