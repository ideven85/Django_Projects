# Generated by Django 5.0.6 on 2024-06-05 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_alter_course_course_name_prerequisites"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="department",
            field=models.CharField(default="CS", max_length=20),
        ),
    ]