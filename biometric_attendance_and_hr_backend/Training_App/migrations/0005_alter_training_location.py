# Generated by Django 5.1 on 2024-08-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Training_App', '0004_alter_training_options_alter_training_employee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]
