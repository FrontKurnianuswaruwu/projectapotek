# Generated by Django 4.2.5 on 2023-09-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mapotik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_apotik', models.CharField(max_length=100)),
                ('alamat_apotik', models.CharField(max_length=200)),
                ('telepon_retail', models.CharField(max_length=20)),
                ('owner', models.CharField(max_length=50)),
                ('kontak_person', models.CharField(max_length=40)),
            ],
        ),
    ]
