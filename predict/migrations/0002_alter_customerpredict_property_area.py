# Generated by Django 4.1.2 on 2022-11-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerpredict",
            name="Property_Area",
            field=models.CharField(
                choices=[
                    ("Urban", "Urban"),
                    ("Semiurban", "Semiurban"),
                    ("Rural", "Rural"),
                ],
                default="",
                max_length=100,
            ),
        ),
    ]