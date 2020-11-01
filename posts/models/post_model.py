from datetime import datetime

from django.db import models


class Post(models.Model):
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.DO_NOTHING,
        related_name="post",
    )
    name = models.CharField(
        "Name of post",
        max_length=512,
    )
    content = models.TextField(
        "Content of post",
        max_length=2048,
    )
    date_creation = models.DateTimeField(
        "Date of creation",
        default=datetime.now,
    )
    date_editing = models.DateTimeField(
        "Date of edit",
        blank=True,
        null=True,
    )
    on_moderation = models.BooleanField(
        "On moderation",
        default=False,
    )

    likes = models.ManyToManyField(
        "users.User",
        related_name="post_user_likes",
        verbose_name="Who like post",
        blank=True,
    )
    dislikes = models.ManyToManyField(
        "users.User",
        related_name="post_user_dislikes",
        verbose_name="Who dislike post",
        blank=True,
    )
    comments = models.ManyToManyField(
        "posts.Comment",
        related_name="post",
        blank=True,
    )
    can_commenting = models.BooleanField(
        "Users can commenting",
        default=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
