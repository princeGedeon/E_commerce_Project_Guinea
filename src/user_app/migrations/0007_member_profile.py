# Generated by Django 4.0.4 on 2022-04-25 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0006_alter_user_type_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/Vendeur/images'),
        ),
    ]
