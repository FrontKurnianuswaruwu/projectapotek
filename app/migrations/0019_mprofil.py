# Generated by Django 4.1.7 on 2023-09-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_mbarang_usertime'),
    ]

    operations = [
        migrations.CreateModel(
            name='mprofil',
            fields=[
                ('id_apotik', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=20)),
                ('alamat', models.CharField(max_length=100)),
                ('gambar', models.ImageField(upload_to='')),
                ('facebook', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('whatsapp', models.CharField(max_length=100)),
            ],
        ),
    ]