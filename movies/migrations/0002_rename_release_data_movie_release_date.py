# Generated by Django 4.0.1 on 2022-01-13 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='release_data',
            new_name='release_date',
        ),
    ]