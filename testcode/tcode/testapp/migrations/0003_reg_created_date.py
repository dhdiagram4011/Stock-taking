# Generated by Django 2.2.2 on 2019-06-27 07:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20190627_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]