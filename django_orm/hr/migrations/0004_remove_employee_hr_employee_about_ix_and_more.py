# Generated by Django 5.0.1 on 2024-01-28 05:34

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_employee_hr_employee_about_ix'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='employee',
            name='hr_employee_about_ix',
        ),
        migrations.AddIndex(
            model_name='employee',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='hr_employee_created_ix', pages_per_range=2),
        ),
    ]
