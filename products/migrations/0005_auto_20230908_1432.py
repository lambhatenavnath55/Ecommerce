# Generated by Django 2.2.7 on 2023-09-08 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20230908_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimages',
            name='product',
        ),
        migrations.AddField(
            model_name='productimages',
            name='product_name',
            field=models.ForeignKey(default=100, on_delete=django.db.models.deletion.PROTECT, to='products.Product'),
            preserve_default=False,
        ),
    ]
