from django.conf.urls import url
from app.usuarios import views

urlpatterns =[
    url(r'^login/$' , views.authentication , name='login'),

]
