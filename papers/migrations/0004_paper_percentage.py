# Generated by Django 4.2.4 on 2023-08-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0003_alter_paper_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='percentage',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]