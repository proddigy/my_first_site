# Generated by Django 4.1.3 on 2022-11-29 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0012_mainpagecarousel_alter_comments_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='photo_1',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='photo_2',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='photo_3',
        ),
        migrations.AlterField(
            model_name='sessions',
            name='film',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sessions', to='films.films'),
        ),
    ]
