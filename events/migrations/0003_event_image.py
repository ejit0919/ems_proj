# Generated by Django 2.1.3 on 2018-11-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.FileField(default='', upload_to='Uploads/', verbose_name='Image'),
        ),
    ]
