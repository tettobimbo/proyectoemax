from django.conf.urls import url
#from app.materiales.views import materialesCreateView, materialesListView, materialesUpdateView, materialesDeleteView
from app.materiales import views

urlpatterns = [
    url(r'^eliminarmaterial/(?P<pk>\d+)/$', views.MaterialesDelete.as_view(), name='MaterialesDelete'),
    url(r'^editarmaterial/(?P<pk>\d+)/$', views.MaterialesUpdate.as_view() , name='MaterialesUpdate'),
    url(r'^crearmaterial', views.MaterialesCreate.as_view() , name='MaterialesCreate'),
    url(r'^listarmaterial', views.MaterialesList.as_view() , name='MaterialesList'),
    url(r'^detalle_material/(?P<pk>\d+)/$', views.MaterialesDetail.as_view() , name='MaterialesDetail'),

]
