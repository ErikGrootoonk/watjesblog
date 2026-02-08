from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    language = models.CharField(max_length=50)
    added_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-added_date"]

    def __str__(self):
        return f"{self.title} by {self.author}"
