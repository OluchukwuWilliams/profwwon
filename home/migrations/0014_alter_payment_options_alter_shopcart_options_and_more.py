# Generated by Django 4.1.7 on 2023-04-20 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_category_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'managed': True, 'verbose_name': 'Payment', 'verbose_name_plural': 'Payment'},
        ),
        migrations.AlterModelOptions(
            name='shopcart',
            options={'managed': True, 'verbose_name': 'Shopcart', 'verbose_name_plural': 'Shopcart'},
        ),
        migrations.AlterModelTable(
            name='payment',
            table='payment',
        ),
        migrations.AlterModelTable(
            name='shopcart',
            table='shopcartr',
        ),
    ]