from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Заголовок', max_length=200,
                             help_text='Введите название сообщества')
    description = models.TextField(
        'Описание',
        max_length=200,
        null=True,
        help_text='Описание')
    slug = models.SlugField(
        'Адрес для страницы',
        null=False,
        unique=True,
        help_text='URL')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        "Дата публикации", auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Follower',
        help_text='Подписчик',
        on_delete=models.CASCADE,
        related_name='follower')
    author = models.ForeignKey(
        User,
        verbose_name='author',
        help_text='Автор',
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'author'], name='unique_follow'),
        ]
