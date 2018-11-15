# Generated by Django 2.1.3 on 2018-11-15 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[(1, 'Student'), (2, 'Faculty'), (3, 'Staff')], default='', max_length=50, verbose_name='')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Designation'),
        ),
    ]
