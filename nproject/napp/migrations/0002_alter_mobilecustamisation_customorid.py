# Generated by Django 4.1.1 on 2022-09-29 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('napp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilecustamisation',
            name='customorID',
            field=models.CharField(default='kkk', max_length=20),
        ),
    ]
