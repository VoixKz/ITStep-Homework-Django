from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator


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
    title = models.CharField(
        verbose_name="Заголовок", 
        max_length=100,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(100),
        ]
    )
    subtitle = models.CharField(
        verbose_name="Подзаголовок", 
        max_length=200,
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(200),
            RegexValidator(
                regex=r'[A-Za-zА-Яа-я]',
                message='Подзаголовок должен содержать буквы.'
            )
        ]
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts', verbose_name="Автор")
    content = models.TextField(
        verbose_name="Текст",
        validators=[
            MinLengthValidator(20),
            RegexValidator(
                regex=r'[A-Za-zА-Яа-я]',
                message='Текст должен содержать буквы.'
            )
        ]
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='posts', verbose_name="Жанр")
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return f"{self.genre} | {self.title}"
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="Пост")
    author = models.CharField(
        verbose_name="Автор", 
        max_length=50,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(50),
            RegexValidator(
                regex=r'[A-Za-zА-Яа-я]',
                message='Имя автора должно содержать буквы.'
            )
        ]
    )
    content = models.TextField(
        verbose_name="Текст",
        validators=[
            MinLengthValidator(5),
            RegexValidator(
                regex=r'[A-Za-zА-Яа-я]',
                message='Комментарий должен содержать буквы.'
            )
        ]
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'