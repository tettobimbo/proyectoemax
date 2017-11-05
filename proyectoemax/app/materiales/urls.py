from django.conf.urls import url
#from app.materiales.views import materialesCreateView, materialesListView, materialesUpdateView, materialesDeleteView
from app.materiales import views

urlpatterns = [
#    url(r'^eliminarmaterial', views.eliminarmaterial, name='eliminarmaterial'),
#    url(r'^editarmaterial', views.modificarmaterial , name='editar_material'),
    url(r'^crearmaterial', views.crearmaterial , name='nuevo_material'),
    url(r'^listarmaterial', views.listarmaterial , name='material_lista'),

]
