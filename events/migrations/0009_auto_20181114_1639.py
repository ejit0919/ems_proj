# Generated by Django 2.1.3 on 2018-11-14 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20181114_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.FileField(blank=True, default='', null=True, upload_to='media/Uploads/', verbose_name='Image'),
        ),
    ]
