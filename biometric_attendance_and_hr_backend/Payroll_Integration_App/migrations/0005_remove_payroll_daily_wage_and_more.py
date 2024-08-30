# Generated by Django 5.1 on 2024-08-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payroll_Integration_App', '0004_alter_payroll_absences_in_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payroll',
            name='daily_wage',
        ),
        migrations.RemoveField(
            model_name='payroll',
            name='working_days_in_month',
        ),
        migrations.AddField(
            model_name='payroll',
            name='working_days',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='absences_in_month',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
