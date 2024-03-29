# Generated by Django 3.2.1 on 2023-01-14 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id_category', models.AutoField(primary_key=True, serialize=False)),
                ('name_category', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.AutoField(primary_key=True, serialize=False)),
                ('name_client', models.CharField(max_length=50)),
                ('last_name_client', models.CharField(max_length=100)),
                ('email_client', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('doc', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Numero de documento')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre de usuario')),
                ('email', models.CharField(blank=True, max_length=60, null=True, verbose_name='Email')),
                ('user_active', models.BooleanField(default=True)),
                ('user_type', models.CharField(max_length=1, verbose_name='Tipo usuario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Product name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Image')),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(db_column='id_category', on_delete=django.db.models.deletion.CASCADE, to='GlobalApi.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_address', models.CharField(max_length=300, verbose_name='Order Address')),
                ('order_date', models.DateField(null=True)),
                ('order_active', models.BooleanField(default=True)),
                ('order_client_id', models.ForeignKey(db_column='id_client', default=0, on_delete=django.db.models.deletion.CASCADE, to='GlobalApi.client')),
                ('order_products', models.ManyToManyField(to='GlobalApi.Products')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='doc_client',
            field=models.ForeignKey(db_column='doc', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id_admin', models.AutoField(primary_key=True, serialize=False)),
                ('name_admin', models.CharField(max_length=50)),
                ('last_name_admin', models.CharField(max_length=100)),
                ('email_admin', models.EmailField(max_length=254)),
                ('doc_admin', models.ForeignKey(db_column='doc', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
