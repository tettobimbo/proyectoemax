
from django.conf.urls import url , include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^herramientas/', include('app.herramientas.urls',namespace='herramientas')),
    url(r'^materiales/', include('app.materiales.urls',namespace='materiales')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
