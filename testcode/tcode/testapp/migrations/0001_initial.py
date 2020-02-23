# Generated by Django 2.1.15 on 2020-02-23 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serverlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('team', models.CharField(max_length=500)),
                ('server_count', models.IntegerField()),
                ('model_name', models.CharField(max_length=500)),
                ('code', models.CharField(max_length=500)),
                ('use_case', models.TextField(max_length=5000)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
