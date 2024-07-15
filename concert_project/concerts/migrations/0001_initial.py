# Generated by Django 5.0.7 on 2024-07-11 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('venue', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SeatingLayout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=100)),
                ('seat_number', models.CharField(max_length=10)),
                ('is_reserved', models.BooleanField(default=False)),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seating_layouts', to='concerts.concert')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='concerts.concert')),
                ('seating_layout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concerts.seatinglayout')),
            ],
        ),
    ]