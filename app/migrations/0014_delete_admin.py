# Generated by Django 4.2.5 on 2023-09-15 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_admin_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='admin',
        ),
    ]