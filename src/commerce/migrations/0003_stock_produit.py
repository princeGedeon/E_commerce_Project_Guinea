# Generated by Django 4.0.4 on 2022-04-25 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='produit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='commerce.product'),
            preserve_default=False,
        ),
    ]
