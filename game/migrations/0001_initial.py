# Generated by Django 4.1 on 2022-08-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_code', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=200)),
                ('join', models.CharField(max_length=200)),
                ('game_status', models.BooleanField(default=False)),
            ],
        ),
    ]
