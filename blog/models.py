from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Tag(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts')


    def __str__(self):
        return self.title

