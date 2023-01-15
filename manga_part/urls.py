from django.urls import path
from manga_part.views import GenreView, TypeOfMangaView,\
    MangaView, MangaDetail, CommentView


urlpatterns = [
    path('api/v1/genres/', GenreView.as_view({"get":"list"})),
    path('api/v1/type/', TypeOfMangaView.as_view({"get":"list"})),
    path('api/v1/manga/', MangaView.as_view({"get":"list"})),
    path('api/v1/manga/<int:pk>/', MangaDetail.as_view({"get":"retrieve"})),
    path('api/v1/comment/',CommentView.as_view({"get":"retrieve", "post": "create"})),
]