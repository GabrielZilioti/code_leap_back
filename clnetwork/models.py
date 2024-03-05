from django.db import models


class CLNetwork(models.Model):
    username = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title
