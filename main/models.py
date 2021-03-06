from django.db import models


class Song(models.Model):
    link = models.URLField(max_length=250)
    email = models.EmailField(verbose_name="email_to")
    created_at = models.DateTimeField(
        verbose_name="request sent", auto_now_add=True, null=True
    )

    def __str__(self):
        return self.link
