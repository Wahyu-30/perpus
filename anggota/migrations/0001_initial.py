# Generated by Django 5.1.1 on 2024-12-06 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anggota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_ang', models.CharField(max_length=4)),
                ('nama_ang', models.CharField(max_length=100)),
                ('jenis_kelamin', models.CharField(max_length=50)),
                ('no_phone', models.CharField(max_length=40)),
                ('alamat', models.CharField(max_length=40)),
                ('angkatan', models.CharField(max_length=4)),
            ],
        ),
    ]
