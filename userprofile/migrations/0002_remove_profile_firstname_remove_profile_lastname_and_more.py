# Generated by Django 4.1.7 on 2023-04-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastname',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='ad', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='ad', max_length=100),
        ),
    ]
