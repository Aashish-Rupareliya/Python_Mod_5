from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from product_management import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('product_management.urls')),
    path('', product_views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
