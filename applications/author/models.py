from django.db import models

class Author(models.Model):
    """Model definition for Author."""

    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        """Meta definition for Author."""

        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f"{self.name} {self.last_name}"


