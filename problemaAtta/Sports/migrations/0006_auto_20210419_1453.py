# Generated by Django 3.1.7 on 2021-04-19 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sports', '0005_remove_sports_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='Sports',
        ),
        migrations.AddField(
            model_name='sports',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='Sports.location'),
        ),
    ]