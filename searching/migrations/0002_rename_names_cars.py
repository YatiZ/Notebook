# Generated by Django 4.1 on 2022-12-20 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("searching", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="names",
            new_name="cars",
        ),
    ]