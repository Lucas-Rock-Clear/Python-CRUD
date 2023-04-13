from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=255)



    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['-id'] 