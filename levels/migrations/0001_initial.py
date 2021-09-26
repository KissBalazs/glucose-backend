# Generated by Django 3.2.7 on 2021-09-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('stop', models.DateTimeField(auto_now_add=True)),
                ('gerat', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ['start'],
            },
        ),
    ]
