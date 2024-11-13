from django.db import models


class Genre(models.Model):
    name = models.CharField(verbose_name="Название жанра", max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Author(models.Model):
    name = models.CharField(verbose_name="Имя автора", max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    subtitle = models.CharField(verbose_name="Подзаголовок", max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts', verbose_name="Автор")
    content = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='posts', verbose_name="Жанр")

    def __str__(self):
        return f"{self.genre} | {self.title}"
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="Пост")
    author = models.CharField(verbose_name="Автор", max_length=50)
    content = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'