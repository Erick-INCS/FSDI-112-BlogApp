from django.db import models

# Create your models here.
class Post(models.Model):
    """
    docstring
    """
    pass
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',
    on_delete=models.CASCADE,)
    body = models.TextField(name='body', default='')

    def __str__(self):
        return self.title