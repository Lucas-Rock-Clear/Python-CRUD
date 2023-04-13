from django.db import models


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=255)



    class Meta():
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'
        ordering = ['-id'] 