# Generated by Django 5.0 on 2024-03-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
