# Generated by Django 4.1.7 on 2023-05-19 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_rename_cources_cource'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cource',
            new_name='Course',
        ),
    ]