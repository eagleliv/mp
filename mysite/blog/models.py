from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length = 150)
    author = models.CharField(max_length = 100)
    body = models.TextField(blank = True)
    date_pub = models.DateTimeField(auto_now_add = True)

#    def get_absolute_url(self):
#        return reverse('post_detail_url', kwargs={'post_id': self.id})

    def __str__(self):
        return self.title
