# Generated by Django 2.1.3 on 2018-11-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0003_auto_20181114_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='parents_permit',
            field=models.FileField(default='', upload_to='reg/', verbose_name='Parents Permit'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='waiver',
            field=models.FileField(default='', upload_to='reg/', verbose_name='Waiver'),
        ),
    ]