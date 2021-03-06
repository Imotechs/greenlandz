# Generated by Django 4.0.1 on 2022-05-01 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmImpliments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(default='media/FarmImpliments/default.jpg', upload_to='media/FarmImpliments')),
                ('local_govt', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('customer_phone', models.CharField(max_length=15)),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_address', models.CharField(max_length=150)),
                ('description', models.TextField(default='All available Tool at Greenlands')),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GreenlandFarms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(default='media/GreenlandFarms/default.jpg', upload_to='media/GreenlandFarms')),
                ('local_govt', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('first_quarter', models.BooleanField(default=True)),
                ('second_quarter', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=3, max_digits=10)),
                ('offer_season', models.CharField(max_length=20)),
                ('offer_gain', models.CharField(max_length=20)),
                ('offer_duration', models.CharField(max_length=20)),
                ('available', models.BooleanField(default=True)),
                ('is_promoted', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(default='A new farm')),
            ],
        ),
        migrations.DeleteModel(
            name='Farm_Tool',
        ),
        migrations.RemoveField(
            model_name='trending',
            name='quarter',
        ),
        migrations.RemoveField(
            model_name='availablejob',
            name='name',
        ),
        migrations.AddField(
            model_name='availablejob',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='availablejob',
            name='photo',
            field=models.ImageField(default='media/Jobs/default.jpg', upload_to='media/Jobs'),
        ),
        migrations.AddField(
            model_name='availablejob',
            name='type_of_work',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='availablejob',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='land',
            name='description',
            field=models.TextField(default='A new Land'),
        ),
        migrations.AlterField(
            model_name='availablejob',
            name='country',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='availablejob',
            name='local_govt',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='availablejob',
            name='state',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.DeleteModel(
            name='Quarter',
        ),
        migrations.DeleteModel(
            name='Trending',
        ),
    ]
