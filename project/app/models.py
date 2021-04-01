from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=255)
    excerpt = models.TextField()

    def __str__(self):
        return self.name
