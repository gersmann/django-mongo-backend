# Generated by Django 4.2.9 on 2024-01-12 08:30

import bson.objectid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("testapp", "0004_remove_dummymodel_json_field_remove_dummymodel_name2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dummymodel",
            name="id",
            field=models.CharField(
                db_column="_id",
                default=bson.objectid.ObjectId,
                max_length=24,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
