# Generated by Django 4.0.1 on 2022-05-01 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_sharespayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharespayment',
            name='country',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
