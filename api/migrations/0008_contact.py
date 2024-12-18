# Generated by Django 5.1.2 on 2024-10-11 12:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
                ('service', models.CharField(choices=[('Web development', 'Web development'), ('Data Analysis', 'Data Analysis'), ('Machine Learning', 'Machine Learning'), ('Mobile Application', 'Mobile Application')], max_length=50)),
                ('message', models.TextField()),
                ('submission_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
