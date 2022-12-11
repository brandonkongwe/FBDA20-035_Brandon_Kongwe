# Generated by Django 4.1.2 on 2022-10-17 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("loans", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("login", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sms_log",
            name="cust_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="login.customer"
            ),
        ),
        migrations.AddField(
            model_name="loan_payment",
            name="cust_id",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="login.customer",
            ),
        ),
        migrations.AddField(
            model_name="loan_payment",
            name="reviewed_by",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"is_staff": True},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="loan_application",
            name="cust_id",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="login.customer",
            ),
        ),
        migrations.AddField(
            model_name="loan_application",
            name="loan_type_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="loans.loan_type"
            ),
        ),
        migrations.AddField(
            model_name="loan_application",
            name="processed_by",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"is_staff": True},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="loan_amortization",
            name="control_number",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="loans.loan_application"
            ),
        ),
    ]
