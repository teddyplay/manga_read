from rest_framework import serializers
from manga_part.models import Manga, TypeOfManga, Genre, Comment
from users.models import User


class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        min_length=2,
        max_length=20,
    )

    class Meta:
        model = User
        fields = ("username",)


class GenresSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(
        min_length=3,
        max_length=50,
    )

    class Meta:
        model = Genre
        fields = [
            "id",
            "genre",
            "manga_list",
        ]


class TypeOfMangaSeializer(serializers.ModelSerializer):
    type_of = serializers.CharField(
        min_length=1,
        max_length=50,
    )

    class Meta:
        model = TypeOfManga
        fields = [
            "id",
            "type_of",
        ]


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.HiddenField(default=serializers.CurrentUserDefault())
    text = serializers.CharField(max_length=500, required=False)
    manga_id = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "text",
            "username_id",
            "username",
            "manga",
            "manga_id",
        ]


class MangaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        min_length=1,
        max_length=70,
    )
    year = serializers.IntegerField(default=0)


    class Meta:
        model = Manga
        fields = [
            "id",
            "name",
            "year",
            "comments",
            # "text",
        ]