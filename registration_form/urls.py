
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include("web.urls", namespace="web")),
    path('admin/', admin.site.urls),
    path('register/', include("registration_completed.urls", namespace="registration_completed")),
    path('user/', include("user.urls", namespace="user")),
]


if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )