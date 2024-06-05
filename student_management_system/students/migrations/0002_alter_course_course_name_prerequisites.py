# Generated by Django 5.0.6 on 2024-06-05 01:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="course_name",
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.CreateModel(
            name="Prerequisites",
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
                (
                    "course_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="selected_course",
                        to="students.course",
                    ),
                ),
                (
                    "prerequisites",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Courses_Required",
                        to="students.course",
                    ),
                ),
            ],
        ),
    ]