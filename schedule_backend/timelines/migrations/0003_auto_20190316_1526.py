# Generated by Django 2.1.5 on 2019-03-16 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timelines', '0002_auto_20190315_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instate',
            name='Interview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_state', to='timelines.Interview'),
        ),
        migrations.AlterUniqueTogether(
            name='timeline',
            unique_together={('interviewTimeline', 'user')},
        ),
    ]
