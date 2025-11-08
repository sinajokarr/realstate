from django.db import models

from django.conf import settings
from django.urls import reverse

class Post(models.Model):
    PUBLISHED = 'pub'
    DRAFT     = 'drf'
    STATUS_CHOICES = [
        (PUBLISHED, 'Published'),
        (DRAFT,     'Draft'),
    ]

    title         = models.CharField(max_length=200)
    text          = models.TextField()
    author        = models.ForeignKey(
                      settings.AUTH_USER_MODEL,
                      on_delete=models.CASCADE,
                      related_name='posts'
                   )
    status        = models.CharField(
                      max_length=3,
                      choices=STATUS_CHOICES,
                      default=PUBLISHED
                   )
    date_created  = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])