# Generated by Django 2.1.3 on 2018-11-15 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181116_0243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='name',
            new_name='designation',
        ),
    ]
