# Generated by Django 2.2.22 on 2021-05-10 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='data_added',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='data_added',
            new_name='date_added',
        ),
    ]