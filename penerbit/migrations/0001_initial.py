# Generated by Django 5.1.1 on 2024-12-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_pen', models.CharField(max_length=4)),
                ('nama_pen', models.CharField(max_length=100)),
                ('alamat_pen', models.CharField(max_length=50)),
                ('kota_pen', models.CharField(max_length=40)),
                ('kontak_pen', models.CharField(max_length=12)),
                ('email_pen', models.CharField(max_length=25)),
            ],
        ),
    ]
