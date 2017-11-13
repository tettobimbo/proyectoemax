from django.conf.urls import url
from app.usuarios import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns =[
    url(r'^login/$' ,views.authentication , name='authentication'),
    url(r'^index/$' , login_required(views.index ), name='index'),
    url(r'^logout/$' , login_required(auth_views.logout) , {'next_page':'/accounts/login'}, name='logout'),
    url(r'^listarusuarios/$' , login_required(views.UsuarioList.as_view()) , name='UsuarioList'),
    url(r'^eliminarusuario/(?P<pk>\d+)/$', login_required(views.UsuarioDelete.as_view()) , name='UsuarioDelete'),
    url(r'^editarusuario/(?P<pk>\d+)/$', login_required(views.UsuarioUpdate.as_view()) , name='UsuarioUpdate'),
    url(r'^crearusuario', login_required(views.UsuarioCreate.as_view()) , name='UsuarioCreate'),
    url(r'^detalleusuario/(?P<pk>\d+)/$', login_required(views.UsuarioDetail.as_view()) , name='UsuarioDetail'),
]
