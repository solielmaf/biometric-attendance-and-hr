# Generated by Django 5.1 on 2024-08-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Departments', '0005_delete_departments_subdepartment_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subdepartment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
