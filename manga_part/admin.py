from django.contrib import admin
from manga_part.models import Genre
from manga_part.models import TypeOfManga
from manga_part.models import Manga
from manga_part.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "manga", "text", "username")
    list_display_links = ("id", "username")
    search_fields = ("username",)
    list_per_page = 3


class MangaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image")
    list_display_links = ("id", "name")
    search_fields = ("name", "year", )
    list_per_page = 12



admin.site.register(Genre)
admin.site.register(TypeOfManga)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Manga, MangaAdmin)
