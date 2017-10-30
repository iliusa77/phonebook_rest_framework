from django.db import models

class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True, default='')
    photo = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ('created',)