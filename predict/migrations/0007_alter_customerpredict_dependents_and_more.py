# Generated by Django 4.1.2 on 2022-11-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0006_alter_customerpredict_dependents_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerpredict",
            name="Dependents",
            field=models.CharField(
                choices=[("0", "0"), ("1", "1"), ("2", "2"), ("3+", "3+")],
                default="",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="customerpredict",
            name="Education",
            field=models.CharField(
                choices=[("Graduate", "Graduate"), ("Not Graduate", "Not Graduate")],
                default="",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="customerpredict",
            name="Gender",
            field=models.CharField(
                choices=[("Male", "Male"), ("Female", "Female")],
                default="",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="customerpredict",
            name="Married",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")], default="", max_length=100
            ),
        ),
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
        migrations.AlterField(
            model_name="customerpredict",
            name="Self_Employed",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")], default="", max_length=100
            ),
        ),
    ]
