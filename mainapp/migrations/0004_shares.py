# Generated by Django 4.0.1 on 2022-05-01 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_remove_availablejob_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
    ]
