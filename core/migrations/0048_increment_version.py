# Generated by Django 4.2.11 on 2024-04-01 19:36

from django.db import migrations


def update_version(apps, schema):
    Constants = apps.get_model("core", "Constants")
    version = Constants.objects.get(key="version")
    version.value = "24.4.1"
    version.save()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0047_increment_version"),
    ]

    operations = [migrations.RunPython(update_version)]