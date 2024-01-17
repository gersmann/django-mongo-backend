# Generated by Django 4.2.9 on 2024-01-17 20:51

from django.db import migrations, models
import django.db.models.deletion
import django_mongodb.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FooModel",
            fields=[
                (
                    "id",
                    django_mongodb.models.ObjectIdAutoField(
                        auto_created=True,
                        db_column="_id",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("json_field", models.JSONField()),
                ("name", models.CharField(max_length=100)),
                ("datetime_field", models.DateTimeField(auto_now_add=True)),
                ("time_field", models.TimeField(auto_now_add=True)),
                ("date_field", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="DifferentTableOneToOne",
            fields=[
                (
                    "dummy_model",
                    models.OneToOneField(
                        db_column="_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="another_extends",
                        serialize=False,
                        to="testapp.foomodel",
                    ),
                ),
                ("extra", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="SameTableChild",
            fields=[
                (
                    "dummy_model_ptr",
                    models.OneToOneField(
                        db_column="_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="child_type",
                        serialize=False,
                        to="testapp.foomodel",
                    ),
                ),
                ("extended", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "testapp_foomodel",
            },
            bases=("testapp.foomodel",),
        ),
        migrations.CreateModel(
            name="SameTableOneToOne",
            fields=[
                (
                    "dummy_model",
                    models.OneToOneField(
                        db_column="_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="extends",
                        serialize=False,
                        to="testapp.foomodel",
                    ),
                ),
                ("extra", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "testapp_foomodel",
            },
        ),
        migrations.CreateModel(
            name="RelatedModel",
            fields=[
                (
                    "id",
                    django_mongodb.models.ObjectIdAutoField(
                        auto_created=True,
                        db_column="_id",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "foo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related",
                        to="testapp.foomodel",
                    ),
                ),
            ],
        ),
    ]
