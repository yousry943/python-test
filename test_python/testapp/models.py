from django.db import models

# Create your models here.

class Posts(models.Model):

    post_title=models.CharField(max_length=255)
    post_description=models.TextField()