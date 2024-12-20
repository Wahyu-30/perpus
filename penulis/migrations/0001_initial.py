# Generated by Django 5.1.1 on 2024-12-20 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='writter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_penul', models.CharField(max_length=4)),
                ('nama_penul', models.CharField(max_length=100)),
                ('alamat_penul', models.CharField(max_length=50)),
                ('kota_penul', models.CharField(max_length=40)),
                ('kontak_penul', models.CharField(max_length=12)),
                ('email_penul', models.CharField(max_length=25)),
            ],
        ),
    ]