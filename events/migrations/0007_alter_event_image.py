# Generated by Django 4.1.7 on 2023-05-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_remove_event_eligibilityfeild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='events/images/'),
        ),
    ]
