# Generated by Django 4.2.7 on 2023-12-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0005_userdeactivation"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="userblock",
            name="unique_user_block",
        ),
        migrations.RemoveConstraint(
            model_name="userfollow",
            name="unique_user_follow",
        ),
        migrations.AddConstraint(
            model_name="userblock",
            constraint=models.UniqueConstraint(
                fields=("from_user", "to_user"), name="unique_account_userblock"
            ),
        ),
        migrations.AddConstraint(
            model_name="userfollow",
            constraint=models.UniqueConstraint(
                fields=("from_user", "to_user"), name="unique_account_userfollow"
            ),
        ),
    ]
