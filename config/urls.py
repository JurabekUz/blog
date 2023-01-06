
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('core.urls')), #asosiy app ga url
    path('members/', include('django.contrib.auth.urls')), #auth uchun url
    path('members/', include('members.urls')), #akkauntlar app iga url

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
