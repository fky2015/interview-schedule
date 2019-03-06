# Generated by Django 2.1.5 on 2019-03-06 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190306_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileclub',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userProfileClub', to='users.Club'),
        ),
        migrations.AlterField(
            model_name='userprofileclub',
            name='userProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userProfileClub', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='userprofileclub',
            unique_together={('userProfile', 'club')},
        ),
    ]
