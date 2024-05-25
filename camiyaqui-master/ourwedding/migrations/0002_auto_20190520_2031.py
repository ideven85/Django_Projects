# Generated by Django 2.2.1 on 2019-05-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourwedding', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='comes_from',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Coming from'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='has_car',
            field=models.BooleanField(default=False, help_text='Do you have a car?', verbose_name='Have car'),
        ),
    ]