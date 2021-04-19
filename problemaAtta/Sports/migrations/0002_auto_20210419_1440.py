# Generated by Django 3.1.7 on 2021-04-19 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='Sports',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='Sports.sports'),
        ),
        migrations.AddField(
            model_name='sports',
            name='Location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='Sports.location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sports',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]