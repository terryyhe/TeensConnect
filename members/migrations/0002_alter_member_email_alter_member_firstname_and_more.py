# Generated by Django 4.0.6 on 2022-07-17 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='member',
            name='firstname',
            field=models.CharField(max_length=128, verbose_name='Firstname'),
        ),
        migrations.AlterField(
            model_name='member',
            name='lastname',
            field=models.CharField(max_length=128, verbose_name='Lastname'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(max_length=50, verbose_name='Phone Number'),
        ),
    ]
