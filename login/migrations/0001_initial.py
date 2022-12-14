# Generated by Django 4.1.2 on 2022-10-17 09:12

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="user_group",
            fields=[
                (
                    "group_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        to="auth.group",
                    ),
                ),
                (
                    "group_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("description", models.TextField()),
            ],
            bases=("auth.group",),
            managers=[("objects", django.contrib.auth.models.GroupManager()),],
        ),
        migrations.CreateModel(
            name="customer",
            fields=[
                (
                    "cust_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("first_name", models.CharField(max_length=250)),
                ("surname", models.CharField(max_length=250)),
                ("complete_address", models.CharField(max_length=250)),
                ("contact_number", models.IntegerField()),
                ("email_address", models.EmailField(default="", max_length=100)),
                ("gender", models.CharField(default="", max_length=30)),
                ("civil_status", models.CharField(max_length=250)),
                ("birthdate", models.DateField()),
                ("age", models.IntegerField()),
                (
                    "profile_pic",
                    models.ImageField(blank=True, null=True, upload_to="img"),
                ),
                (
                    "account_status",
                    models.CharField(
                        choices=[("Active", "Active"), ("Inactive", "Inactive")],
                        default="",
                        max_length=100,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        default="user=request.user.username",
                        limit_choices_to={"is_staff": False},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
