from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("noteApp.urls")),
    path("search/", include("searching.urls")),
    path('data/',include("user.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
