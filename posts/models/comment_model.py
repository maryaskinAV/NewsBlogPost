from django.db import models


class Comment(models.Model):
    """ Model of comment for the post"""

    author_comment = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    text = models.TextField(max_length=300)
    answer = models.ManyToManyField(
        "self",
        verbose_name="Answer",
        symmetrical=True,
        blank=True,
    )
    supporting = models.ManyToManyField(
        "users.User",
        verbose_name="Поддержавшие",
        blank=True,
        related_name="user_comment_supporting",
    )

    unsupporting = models.ManyToManyField(
        "users.User",
        verbose_name="Не поддержавшие",
        blank=True,
        related_name="user_comment_unsupporting",
    )

    def __str__(self) -> str:
        return f"{self.author_comment} -> {self.text[:30]}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
