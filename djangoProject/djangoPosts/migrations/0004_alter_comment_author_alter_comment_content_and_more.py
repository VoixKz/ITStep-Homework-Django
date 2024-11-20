# Generated by Django 5.0.1 on 2024-11-20 16:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoPosts', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(50), django.core.validators.RegexValidator(message='Имя автора должно содержать буквы.', regex='[A-Za-zА-Яа-я]')], verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(5), django.core.validators.RegexValidator(message='Комментарий должен содержать буквы.', regex='[A-Za-zА-Яа-я]')], verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(20), django.core.validators.RegexValidator(message='Текст должен содержать буквы.', regex='[A-Za-zА-Яа-я]')], verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(200), django.core.validators.RegexValidator(message='Подзаголовок должен содержать буквы.', regex='[A-Za-zА-Яа-я]')], verbose_name='Подзаголовок'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(100)], verbose_name='Заголовок'),
        ),
    ]