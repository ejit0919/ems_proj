# Generated by Django 2.1.3 on 2018-11-14 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='status',
            field=models.CharField(default='Pending', max_length=11, verbose_name='Status'),
        ),
    ]