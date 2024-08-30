# Generated by Django 5.1 on 2024-08-15 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employee', '0007_remove_employee_basic_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('basic_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('allowance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('deductions', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('gross_salary', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('net_salary', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('pay_period_start_date', models.DateField()),
                ('pay_period_end_date', models.DateField()),
                ('payment_date', models.DateField()),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payrolls', to='Employee.employee')),
            ],
            options={
                'ordering': ['pay_period_end_date'],
            },
        ),
    ]
