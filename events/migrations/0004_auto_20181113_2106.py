# Generated by Django 2.1.3 on 2018-11-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.FileField(blank=True, default='', null=True, upload_to='Uploads/', verbose_name='Image'),
        ),
    ]
