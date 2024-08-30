# Generated by Django 5.0.6 on 2024-08-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Departments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departments',
            name='department_id',
        ),
        migrations.AlterField(
            model_name='departments',
            name='department_name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
