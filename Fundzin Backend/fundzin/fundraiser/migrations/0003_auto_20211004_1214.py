# Generated by Django 3.2.7 on 2021-10-04 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fundraiser", "0002_auto_20211004_1208"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fundraiserimages",
            old_name="creator",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="fundraisermilestones",
            old_name="creator",
            new_name="user",
        ),
    ]
