# Generated by Django 4.1.2 on 2022-10-19 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("author", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("release_date", models.DateField()),
                ("cover", models.ImageField(upload_to="cover")),
                ("visits", models.IntegerField()),
                ("author", models.ManyToManyField(to="author.author")),
                ("category", models.ManyToManyField(to="book.category")),
            ],
            options={
                "verbose_name": "Book",
                "verbose_name_plural": "Books",
            },
        ),
    ]