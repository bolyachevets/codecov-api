# Generated by Django 2.1.3 on 2020-09-16 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codecov_auth', '0009_session_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='student_created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='student_updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]