# Generated by Django 2.2.4 on 2019-08-24 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timelines', '0009_auto_20190824_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instate',
            name='membership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_state', to='users.Membership'),
        ),
    ]