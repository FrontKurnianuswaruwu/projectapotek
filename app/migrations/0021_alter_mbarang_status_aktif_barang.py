# Generated by Django 4.2.5 on 2023-09-20 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_mprofil_gambar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mbarang',
            name='status_aktif_barang',
            field=models.CharField(max_length=100),
        ),
    ]
