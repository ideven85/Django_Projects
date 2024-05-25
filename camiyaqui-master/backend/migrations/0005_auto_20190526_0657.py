# Generated by Django 2.2.1 on 2019-05-26 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_visits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to=settings.AUTH_USER_MODEL),
        ),
    ]
