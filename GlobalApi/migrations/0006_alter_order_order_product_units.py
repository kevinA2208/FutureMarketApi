# Generated by Django 3.2.1 on 2023-01-19 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GlobalApi', '0005_rename_order_products_order_order_product_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_product_units',
            field=models.ManyToManyField(to='GlobalApi.ProductUnits'),
        ),
    ]