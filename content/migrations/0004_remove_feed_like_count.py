# Generated by Django 4.1.7 on 2023-05-23 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0003_bookmark_like_reply"),
    ]

    operations = [
        migrations.RemoveField(model_name="feed", name="like_count",),
    ]
