# Generated by Django 4.1.7 on 2023-03-04 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Coffee",
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
                ("name", models.CharField(max_length=200)),
                ("year", models.IntegerField()),
                ("caffine_content", models.FloatField()),
                ("caffine_percentage", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("text", models.TextField()),
                ("rating", models.FloatField()),
                (
                    "coffee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="aacoffee.coffee",
                    ),
                ),
            ],
        ),
    ]
