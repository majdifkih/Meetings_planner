# Generated by Django 5.1.1 on 2024-09-19 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('floor', models.IntegerField()),
                ('room_number', models.IntegerField()),
            ],
        ),
    ]
