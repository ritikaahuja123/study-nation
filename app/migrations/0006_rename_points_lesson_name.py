# Generated by Django 4.2.6 on 2023-11-02 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_lesson_video"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lesson", old_name="points", new_name="name",
        ),
    ]
