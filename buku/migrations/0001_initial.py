# Generated by Django 5.1.1 on 2024-11-01 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_buku', models.CharField(max_length=4)),
                ('judul_buku', models.CharField(max_length=100)),
                ('pengarang', models.CharField(max_length=50)),
                ('penerbit', models.CharField(max_length=40)),
                ('tahun', models.CharField(max_length=4)),
            ],
        ),
    ]