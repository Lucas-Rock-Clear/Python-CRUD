from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=255)
    book_price = models.IntegerField()
    book_description = models.CharField(max_length=1000)
    author = models.ForeignKey('book_api.Author', on_delete=models.CASCADE, default=None, null=True, blank=True)
    publisher = models.ForeignKey('book_api.Publisher', on_delete=models.CASCADE, default=None, null=True, blank=True)


    class Meta:
        verbose_name = 'Book' #📗
        verbose_name_plural = 'Books' #📚
        ordering = ['-id'] 


