# Generated by Django 4.1.6 on 2023-04-27 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Meal",
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
                ("meal_name", models.CharField(max_length=200)),
                ("prep_time", models.FloatField()),
                ("servings", models.IntegerField()),
                ("ingredients", models.TextField(default="None")),
                ("directions", models.TextField()),
                ("image", models.TextField(default="None")),
                (
                    "meal_type",
                    models.CharField(
                        choices=[("B", "Breakfast"), ("L", "Lunch"), ("D", "Dinner")],
                        default="D",
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
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
                ("question_text", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Nutrition",
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
                ("nut_text", models.CharField(max_length=200)),
                ("total_calories", models.IntegerField()),
                ("fat_grams", models.IntegerField()),
                ("carb_grams", models.IntegerField()),
                ("protein_grams", models.IntegerField()),
                (
                    "meal_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="meals.meal"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Choice",
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
                ("choice_text", models.CharField(max_length=200)),
                ("searches", models.IntegerField(default=0)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="meals.question"
                    ),
                ),
            ],
        ),
    ]
