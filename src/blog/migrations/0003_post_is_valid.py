# Generated by Django 4.0.4 on 2022-04-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comments_post_reponse_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
    ]