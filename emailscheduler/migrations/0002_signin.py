# Generated by Django 4.0.3 on 2022-04-04 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailscheduler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
