# Generated by Django 4.1.3 on 2022-11-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_films_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
