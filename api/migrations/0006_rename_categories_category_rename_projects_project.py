# Generated by Django 5.1.2 on 2024-10-11 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_categories_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
