# Generated by Django 3.2.7 on 2021-10-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fundraiser",
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
                ("user", models.EmailField(max_length=255, unique=True)),
                ("fundraiser_domain", models.CharField(max_length=255)),
                ("creator_location", models.CharField(max_length=255)),
                ("contact_number_country_code", models.CharField(max_length=5)),
                ("contact_number", models.CharField(max_length=10)),
                ("verified_mobile_number", models.BooleanField(default=False)),
                ("title", models.CharField(max_length=255)),
                ("cause", models.CharField(max_length=255)),
                ("story", models.CharField(max_length=5000)),
                ("target_amount", models.IntegerField()),
                (
                    "political_or_religious_inclination",
                    models.BooleanField(default=False),
                ),
                ("add_upi", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="FundraiserImages",
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
                ("creator", models.EmailField(max_length=255)),
                ("image_id", models.IntegerField()),
                ("img", models.ImageField(upload_to="imgs/fundraisers/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="FundraiserMilestones",
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
                ("creator", models.EmailField(max_length=255)),
                ("milestone_id", models.IntegerField()),
                ("milestone_title", models.CharField(max_length=255)),
                ("milestone_desc", models.CharField(max_length=255)),
                ("milestone_release_amount", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
