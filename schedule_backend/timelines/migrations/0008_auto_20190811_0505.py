# Generated by Django 2.2.4 on 2019-08-11 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelines', '0007_auto_20190810_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviewtimeline',
            name='title',
        ),
        migrations.AddField(
            model_name='interviewtimeline',
            name='remarks',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='interviewtimeline',
            name='location',
            field=models.CharField(max_length=100, verbose_name='面试地点'),
        ),
    ]
