# Generated by Django 4.2.3 on 2023-08-01 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='title',
            new_name='first_name',
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]