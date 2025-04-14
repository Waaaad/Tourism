# Generated by Django 4.2.20 on 2025-04-14 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('event', models.CharField(max_length=100)),
                ('event_title', models.CharField(max_length=100)),
                ('event_id', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
