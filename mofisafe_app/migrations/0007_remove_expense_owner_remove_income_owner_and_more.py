# Generated by Django 5.0.6 on 2024-05-19 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mofisafe_app', '0006_remove_budget_user_id_remove_expense_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='income',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Budget',
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.DeleteModel(
            name='Income',
        ),
    ]