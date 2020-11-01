# Generated by Django 3.1.2 on 2020-11-01 18:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(max_length=300)),
                (
                    "answer",
                    models.ManyToManyField(
                        blank=True,
                        related_name="_comment_answer_+",
                        to="posts.Comment",
                        verbose_name="Answer",
                    ),
                ),
                (
                    "author_comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "supporting",
                    models.ManyToManyField(
                        blank=True,
                        related_name="user_comment_supporting",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Поддержавшие",
                    ),
                ),
                (
                    "unsupporting",
                    models.ManyToManyField(
                        blank=True,
                        related_name="user_comment_unsupporting",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Не поддержавшие",
                    ),
                ),
            ],
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=512, verbose_name="Name of post")),
                (
                    "content",
                    models.TextField(max_length=2048, verbose_name="Content of post"),
                ),
                (
                    "date_creation",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="Date of creation"
                    ),
                ),
                (
                    "date_editing",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Date of edit"
                    ),
                ),
                (
                    "on_moderation",
                    models.BooleanField(default=False, verbose_name="On moderation"),
                ),
                (
                    "can_commenting",
                    models.BooleanField(
                        default=True, verbose_name="Users can commenting"
                    ),
                ),
                (
                    "comments",
                    models.ManyToManyField(
                        blank=True, related_name="post", to="posts.Comment"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="post",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Post",
                "verbose_name_plural": "Posts",
            },
        ),
    ]
