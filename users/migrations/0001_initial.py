# Generated by Django 4.0.1 on 2022-04-14 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(blank=True, max_length=30)),
                ('email_address', models.CharField(blank=True, max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('how_can_we_help_you', models.TextField(blank=True)),
            ],
        ),
    ]