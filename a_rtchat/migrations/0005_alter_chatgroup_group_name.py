# Generated by Django 5.0.7 on 2024-07-26 13:44

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_rtchat", "0004_alter_chatgroup_group_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatgroup",
            name="group_name",
            field=models.CharField(
                default=shortuuid.main.ShortUUID.uuid, max_length=128, unique=True
            ),
        ),
    ]
