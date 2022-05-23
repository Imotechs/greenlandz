# Generated by Django 4.0.1 on 2022-05-01 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0004_shares'),
        ('users', '0003_alter_farmspayment_farm'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharesPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=10)),
                ('work_status', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=30)),
                ('id_number', models.CharField(max_length=25)),
                ('id_type', models.CharField(max_length=15)),
                ('DOBd', models.CharField(max_length=4)),
                ('DOBm', models.CharField(max_length=5)),
                ('DOBy', models.CharField(max_length=5)),
                ('gender', models.CharField(max_length=15)),
                ('payment_method', models.CharField(max_length=15)),
                ('acc_number', models.CharField(max_length=15)),
                ('bank', models.CharField(max_length=15)),
                ('acc_type', models.CharField(max_length=15)),
                ('transaction_id', models.CharField(blank=True, max_length=20)),
                ('cost', models.DecimalField(decimal_places=3, max_digits=10)),
                ('is_id', models.BooleanField(default=False)),
                ('is_valid', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('shares', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.shares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]