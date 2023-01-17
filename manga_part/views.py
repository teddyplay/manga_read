from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets

from manga_part.models import Genre,Manga,TypeOfManga,Comment
from manga_part.serializers import GenresSerializer, TypeOfMangaSeializer, MangaSerializer, CommentSerializer
from manga_part.pagination import MangaPagination
from users.permissions import IsOwnerPermission
# from .services import GenreService


class GenreView(viewsets.ModelViewSet):
    """This class handles the views for the Genre model."""
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
    # genre = GenreService()
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly,]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["genre"]


class TypeOfMangaView(viewsets.ModelViewSet):
    """This class handles the views for the TypeOfManga model."""
    queryset = TypeOfManga.objects.all()
    serializer_class = TypeOfMangaSeializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly,]


class MangaView(viewsets.ModelViewSet):
    """This class handles the views for the Manga model."""
    queryset = Manga.objects.select_related("type_of_manga").all()
    serializer_class = MangaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name", "genre"]
    pagination_class = MangaPagination
    permission_classes = [IsAuthenticatedOrReadOnly,]
    authentication_classes = [JWTAuthentication,]


class MangaDetail(viewsets.ModelViewSet):
    """This class handles the views for the detail of the Manga model. """
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get(self, request, pk):
        '''It overrides the default get method to handle retrieval of a specific manga instance by primary key (pk)'''
        post = Manga.objects.get(pk=pk)
        serializer = MangaSerializer(data=request.data)
        serializer.save(post=post)
        return Response(serializer.data)


class CommentView(viewsets.ModelViewSet):
    '''CommentView class handles the CRUD operations for the Comment model using the CommentSerializer'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerPermission,]
