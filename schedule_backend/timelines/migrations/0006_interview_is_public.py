# Generated by Django 2.1.5 on 2019-03-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelines', '0005_auto_20190316_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name="if it's public"),
        ),
    ]