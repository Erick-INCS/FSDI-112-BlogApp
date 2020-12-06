from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    """
    docstring
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',
    on_delete=models.CASCADE,)
    body = models.TextField(name='body', default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        docstring
        """
        return reverse('post_detail', args=[str(self.id)])