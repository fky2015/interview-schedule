# Generated by Django 2.2 on 2019-04-08 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timelines', '0003_auto_20190408_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='out_state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='interview', to='users.Membership'),
        ),
    ]
