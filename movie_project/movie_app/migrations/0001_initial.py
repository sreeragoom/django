# Generated by Django 4.2.9 on 2024-01-31 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                ("name", models.CharField(max_length=250, unique=True)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                ("description", models.TextField(blank=True)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Movies",
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
                ("title", models.CharField(max_length=300, unique=True)),
                ("slug", models.SlugField(max_length=300, unique=True)),
                ("poster", models.ImageField(upload_to="poster_pic")),
                ("year", models.DateField()),
                ("description", models.TextField(max_length=700)),
                ("actors", models.TextField()),
                ("links", models.TextField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movie_app.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "movies",
                "verbose_name_plural": "moviess",
                "ordering": ("title",),
            },
        ),
    ]