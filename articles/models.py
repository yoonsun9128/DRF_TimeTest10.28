
from django.db import models


# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(models, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return str(self.title)