# Generated by Django 5.1 on 2024-08-20 06:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leave_Management_App', '0002_remove_leave_leave_id_leave_approved_by_leave_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='applied_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
