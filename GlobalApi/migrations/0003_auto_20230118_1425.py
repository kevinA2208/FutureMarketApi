# Generated by Django 3.2.1 on 2023-01-18 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GlobalApi', '0002_alter_categories_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Stock'),
        ),
        migrations.CreateModel(
            name='ProductUnits',
            fields=[
                ('product_unit_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_unit_state', models.CharField(max_length=10)),
                ('product_id', models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.CASCADE, to='GlobalApi.products')),
            ],
        ),
    ]
