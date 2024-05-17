# Generated by Django 5.0.6 on 2024-05-14 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mofisafe_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='category',
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(default=['Food', 'Emergency', 'Clothing', 'Housing', 'Health', 'Others'], max_length=100),
        ),
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.CharField(default=['Freelancing', 'Salary', 'Others'], max_length=100),
        ),
    ]
