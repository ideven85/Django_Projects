# Generated by Django 2.2.4 on 2019-08-08 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_photo_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
