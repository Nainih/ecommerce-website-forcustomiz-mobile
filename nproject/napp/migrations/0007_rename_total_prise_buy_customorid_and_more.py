# Generated by Django 4.1.2 on 2022-10-13 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('napp', '0006_buy_qty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buy',
            old_name='total_prise',
            new_name='customorID',
        ),
        migrations.RenameField(
            model_name='buy',
            old_name='productId',
            new_name='productID',
        ),
        migrations.RemoveField(
            model_name='buy',
            name='address',
        ),
        migrations.RemoveField(
            model_name='buy',
            name='qty',
        ),
        migrations.AddField(
            model_name='buy',
            name='Address',
            field=models.CharField(default='not address contact by email', max_length=20),
        ),
    ]
