# Generated by Django 4.0.1 on 2022-05-01 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_sharespayment_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharespayment',
            name='country',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
