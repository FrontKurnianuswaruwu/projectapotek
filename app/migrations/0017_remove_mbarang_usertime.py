# Generated by Django 4.2.5 on 2023-09-15 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_admin_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mbarang',
            name='usertime',
        ),
    ]
