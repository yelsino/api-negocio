
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static


from tienda.views import ProductoViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)