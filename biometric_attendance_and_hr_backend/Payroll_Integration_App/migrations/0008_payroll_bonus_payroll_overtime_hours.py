# Generated by Django 5.1 on 2024-08-29 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payroll_Integration_App', '0007_remove_payroll_daily_wage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='bonus',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='payroll',
            name='overtime_hours',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
