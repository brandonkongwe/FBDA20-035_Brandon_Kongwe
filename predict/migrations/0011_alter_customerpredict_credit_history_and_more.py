# Generated by Django 4.1.2 on 2022-11-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0010_alter_customerpredict_credit_history_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerpredict",
            name="Credit_History",
            field=models.PositiveIntegerField(choices=[(0, 0), (1, 1)], default=0),
        ),
        migrations.AlterField(
            model_name="customerpredict",
            name="Dependents",
            field=models.IntegerField(
                choices=[(0, "0"), (1, "1"), (2, "2"), (3, "3+")], default=""
            ),
        ),
        migrations.AlterField(
            model_name="customerpredict",
            name="Education",
            field=models.IntegerField(
                choices=[(1, "Graduate"), (0, "Not Graduate")], default=""
            ),
        ),
        migrations.AlterField(
            model_name="customerpredict",
            name="Gender",
            field=models.IntegerField(choices=[(0, "Male"), (1, "Female")], default=""),
        ),
        migrations.AlterField(
            model_name="customerpredict",
            name="Married",
            field=models.IntegerField(choices=[(1, "Yes"), (0, "No")], default=""),
        ),
        migrations.AlterField(
            model_name="customerpredict",
            name="Property_Area",
            field=models.IntegerField(
                choices=[(0, "Urban"), (1, "Semiurban"), (2, "Rural")], default=""
            ),
        ),
        migrations.AlterField(
            model_name="customerpredict",
            name="Self_Employed",
            field=models.IntegerField(choices=[(1, "Yes"), (0, "No")], default=""),
        ),
    ]
