# Generated by Django 4.2.5 on 2023-09-13 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_mjenis'),
    ]

    operations = [
        migrations.CreateModel(
            name='msatuan',
            fields=[
                ('kode_satuan', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nama_satuan', models.CharField(max_length=50)),
                ('nama_singkat', models.CharField(max_length=100)),
                ('usertime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
