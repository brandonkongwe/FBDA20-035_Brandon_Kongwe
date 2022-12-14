# Generated by Django 4.1.2 on 2022-10-26 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("loans", "0004_alter_loan_application_remarks_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="loan_application",
            name="user",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"is_staff": False},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customer_loan",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
