# Generated by Django 2.2.4 on 2019-08-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourwedding', '0003_auto_20190520_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='needs_van',
            field=models.BooleanField(default=False, help_text='Do you need transport?', verbose_name='Van'),
        ),
    ]