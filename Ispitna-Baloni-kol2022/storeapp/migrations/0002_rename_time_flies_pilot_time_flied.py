# Generated by Django 4.2 on 2023-05-25 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("storeapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pilot", old_name="time_flies", new_name="time_flied",
        ),
    ]