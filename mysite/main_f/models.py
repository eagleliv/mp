from django.db import models

class PassBase(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 16)

    def __str__(self):
        return self.name
