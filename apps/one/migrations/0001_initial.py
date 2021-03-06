# Generated by Django 3.2.8 on 2021-10-19 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('response_time', models.DateTimeField(blank=True, null=True)),
                ('path', models.CharField(blank=True, max_length=255, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('request', models.JSONField(default=dict)),
                ('response', models.JSONField(default=dict)),
                ('response_code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
    ]
