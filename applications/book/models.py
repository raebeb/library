from django.db import models
from django.forms import ImageField

from ..author.models import Author

class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Book(models.Model):
    """Model definition for Book."""

    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, 
        null=True,
        blank=True,
        related_name="books",
        on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    cover = models.ImageField(upload_to="cover")
    visits = models.IntegerField()

    class Meta:
        """Meta definition for Book."""

        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

