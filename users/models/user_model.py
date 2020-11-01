from django.contrib.auth.models import AbstractUser
from django.db import models

SEX_TYPE = (
    (0, "woman"),
    (1, "man"),
)


class User(AbstractUser):
    avatar = models.ImageField(
        "User avatar",
        upload_to="users/avatar/",
        default="images/default_avatar.png",
        blank=True,
        null=True,
    )
    bio = models.TextField(
        "Biography",
        max_length=500,
        blank=True,
        null=True,
    )
    date_birthday = models.DateField(
        "User birthday",
        blank=True,
        null=True,
    )
    sex = models.SmallIntegerField(
        "Sex user",
        choices=SEX_TYPE,
        blank=True,
        null=True,
    )
    friends = models.ManyToManyField(
        "self",
        verbose_name="friends",
        symmetrical=True,
        blank=True,
    )
    followers = models.ManyToManyField(
        "self",
        verbose_name="followers",
        symmetrical=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
