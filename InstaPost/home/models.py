from django.db import models

# Create your models here.
class Post(models.Model):
    heading = models.CharField(max_length=35)
    paragraph = models.TextField(blank=False)
    pubdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading
