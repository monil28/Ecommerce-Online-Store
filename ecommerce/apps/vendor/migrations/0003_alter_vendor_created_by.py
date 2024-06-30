# Generated by Django 5.0.3 on 2024-04-07 06:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendor", "0002_alter_vendor_created_by"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="created_by",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="vendor_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
