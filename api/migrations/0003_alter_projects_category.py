# Generated by Django 5.1.2 on 2024-10-11 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_projects_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.categories'),
        ),
    ]