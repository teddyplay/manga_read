from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Manga import settings
from Manga.settings.base import STATIC_URL


urlpatterns = ([
    path('admin/', admin.site.urls),
    path('' , include("users.urls")),
    path('' , include("manga_part.urls")),
]+ static(settings.base.STATIC_URL, document_url=settings.base.STATIC_URL)
+ static(settings.base.MEDIA_URL, document_root=settings.base.MEDIA_ROOT)
)

