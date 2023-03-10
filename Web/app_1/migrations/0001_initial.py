# Generated by Django 4.1.7 on 2023-03-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserQueryRequest",
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
                ("query_text", models.CharField(max_length=1024)),
                ("audio_wave_file", models.FileField(upload_to="audio_wave_files")),
            ],
        ),
    ]