# Generated by Django 4.0.4 on 2022-04-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenu',
            field=models.TextField(max_length=2000),
        ),
    ]
