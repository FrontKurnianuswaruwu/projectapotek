# Generated by Django 4.2.5 on 2023-09-12 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_mapotik_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='mjenis',
            fields=[
                ('kode_jenis', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nama_jenis', models.CharField(max_length=100)),
                ('kode_kelompok', models.CharField(max_length=4)),
                ('status_ppn', models.CharField(max_length=20)),
                ('usertime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]