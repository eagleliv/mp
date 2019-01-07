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


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = 'comments', on_delete = 'CASCADE')
    name = models.CharField(max_length = 80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
