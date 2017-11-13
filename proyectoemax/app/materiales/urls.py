from django.conf.urls import url
#from app.materiales.views import materialesCreateView, materialesListView, materialesUpdateView, materialesDeleteView
from app.materiales import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    url(r'^eliminarmaterial/(?P<pk>\d+)/$', login_required(views.MaterialesDelete.as_view()), name='MaterialesDelete'),
    url(r'^editarmaterial/(?P<pk>\d+)/$', login_required(views.MaterialesUpdate.as_view()) , name='MaterialesUpdate'),
    url(r'^crearmaterial', login_required(views.MaterialesCreate.as_view()) , name='MaterialesCreate'),
    url(r'^listarmaterial', login_required(views.MaterialesList.as_view()) , name='MaterialesList'),
    url(r'^detalle_material/(?P<pk>\d+)/$', login_required(views.MaterialesDetail.as_view()) , name='MaterialesDetail'),

]
