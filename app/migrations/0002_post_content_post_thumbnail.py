# Generated by Django 4.1 on 2022-08-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="content",
            field=models.TextField(default="no_content"),
        ),
        migrations.AddField(
            model_name="post",
            name="thumbnail",
            field=models.TextField(default="no_thumbnail"),
        ),
    ]
