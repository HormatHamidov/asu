# Generated by Django 4.1.3 on 2023-01-14 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid
import zaida.verification.models.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RegistrationVerification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, unique=True)),
                (
                    "email",
                    models.EmailField(
                        db_index=True, max_length=254, verbose_name="email"
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        max_length=6,
                        validators=[
                            zaida.verification.models.base.code_validator
                        ],
                        verbose_name="code",
                    ),
                ),
                (
                    "date_verified",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="date verified"
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date modified"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date created"
                    ),
                ),
                (
                    "date_completed",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="date completed"
                    ),
                ),
                (
                    "nulled_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="verification.registrationverification",
                        verbose_name="nulled by",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "registration verification",
                "verbose_name_plural": "registration verifications",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PasswordResetVerification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, unique=True)),
                (
                    "email",
                    models.EmailField(
                        db_index=True, max_length=254, verbose_name="email"
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        max_length=6,
                        validators=[
                            zaida.verification.models.base.code_validator
                        ],
                        verbose_name="code",
                    ),
                ),
                (
                    "date_verified",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="date verified"
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date modified"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date created"
                    ),
                ),
                (
                    "date_completed",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="date completed"
                    ),
                ),
                (
                    "nulled_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="verification.passwordresetverification",
                        verbose_name="nulled by",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "password reset verification",
                "verbose_name_plural": "password reset verifications",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EmailVerification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, unique=True)),
                (
                    "email",
                    models.EmailField(
                        db_index=True, max_length=254, verbose_name="email"
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        max_length=6,
                        validators=[
                            zaida.verification.models.base.code_validator
                        ],
                        verbose_name="code",
                    ),
                ),
                (
                    "date_verified",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="date verified"
                    ),
                ),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date modified"
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date created"
                    ),
                ),
                (
                    "nulled_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="verification.emailverification",
                        verbose_name="nulled by",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "email verification",
                "verbose_name_plural": "email verifications",
                "abstract": False,
            },
        ),
        migrations.AddConstraint(
            model_name="registrationverification",
            constraint=models.UniqueConstraint(
                fields=("email", "code"),
                name="registrationverification_unique_email_and_code",
            ),
        ),
        migrations.AddConstraint(
            model_name="passwordresetverification",
            constraint=models.UniqueConstraint(
                fields=("email", "code"),
                name="passwordresetverification_unique_email_and_code",
            ),
        ),
        migrations.AddConstraint(
            model_name="emailverification",
            constraint=models.UniqueConstraint(
                fields=("email", "code"),
                name="emailverification_unique_email_and_code",
            ),
        ),
    ]