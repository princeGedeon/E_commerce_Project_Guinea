# Generated by Django 4.0.4 on 2022-04-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_stock_produit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='total_price',
            field=models.IntegerField(),
        ),
    ]