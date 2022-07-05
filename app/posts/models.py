from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    episodes = models.IntegerField()

    def __str__(self):
        return self.title