# Generated by Django 4.2.2 on 2023-06-23 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("video", "0003_result_error"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="result",
            name="error",
        ),
        migrations.AddField(
            model_name="result",
            name="error_code",
            field=models.IntegerField(default=0),
        ),
    ]