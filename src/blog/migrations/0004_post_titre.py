# Generated by Django 4.0.4 on 2022-04-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_is_valid'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='titre',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]