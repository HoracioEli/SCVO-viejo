# Generated by Django 5.0.4 on 2024-05-01 14:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("certificados", "0002_poliza_cuit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="poliza",
            name="CUIT",
            field=models.CharField(max_length=20),
        ),
    ]
