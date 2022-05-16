from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=90, verbose_name="Post Title")
    content = models.TextField(verbose_name="Post Content")
    published_date = models.DateTimeField(verbose_name="Post Published Date")

    def __str__(self):
        return self.title
