# Generated by Django 4.2.2 on 2023-07-21 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("deals", "0002_remove_task_description_remove_task_status_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Deal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deal_label", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "deal_message",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "end_date",
                    models.DateField(
                        default=datetime.datetime(
                            2023,
                            7,
                            31,
                            17,
                            33,
                            57,
                            872292,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                (
                    "file",
                    models.FileField(blank=True, null=True, upload_to="deals/files"),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Task",
        ),
    ]
