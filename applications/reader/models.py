from django.db import models

from applications.book.models import Book

class Reader(models.Model):
    """Model definition for Reader."""

    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        """Meta definition for Reader."""

        verbose_name = 'Reader'
        verbose_name_plural = 'Readers'

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Loan(models.Model):
    """Model definition for Loan."""

    reader = models.ForeignKey(
        Reader, 
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name="loan")
    book = models.ForeignKey(
        Book, 
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name="loan")
    date_loan = models.DateField(auto_now=True, auto_now_add=False)
    date_return = models.DateField(auto_now=False, auto_now_add=False)
    returned = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        """Meta definition for Loan."""

        verbose_name = 'Loan'
        verbose_name_plural = 'Loans'

    def __str__(self):
        """Unicode representation of Loan."""
        pass
