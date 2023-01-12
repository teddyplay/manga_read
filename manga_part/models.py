from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=50, verbose_name="Жанр",blank=True, name="genre")

    @property
    def manga_list(self):
        return self.mangas.all().count()

    def __str__(self):
        return f'Жанр:{self.genre}'


class TypeOfManga(models.Model):
    type_of = models.CharField(max_length=50, verbose_name="Тип")

    def __str__(self):
        return f'Тип: {self.type_of}'


class Manga(models.Model):
    name = models.CharField(max_length=60)
    year = models.IntegerField(verbose_name="Год выпуска")
    image = models.ImageField(default="", verbose_name="Изображение")
    create = models.DateField(auto_now_add=True,verbose_name="Дата содания")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="mangas")
    type_of_manga = models.ForeignKey(TypeOfManga, on_delete=models.CASCADE, verbose_name="Тип")

    @property
    def comments(self):
        return self.comment_set.all().values()

    def __str__(self):
        return f'Манга: {self.name}'


class Comment(models.Model):
    manga = models.ForeignKey("manga_part.Manga", on_delete=models.CASCADE)
    text = models.TextField(max_length=400, verbose_name="Комменатрии")
    username = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username} Прокомментировал запись {self.manga}'


# Create your models here.
