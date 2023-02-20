# Generated by Django 4.1.7 on 2023-02-20 00:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]

# Manually deleted the contacts db that wasn't migrating as intended via pgadmin. Running a "fake" migration repopulated the empty db and rescued the Contact section.

# https://docs.djangoproject.com/en/dev/ref/django-admin/#migrate
# --fake
# Marks the migrations up to the target one (following the rules above) as applied, but without actually running the SQL to change your database schema.

# This is intended for advanced users to manipulate the current migration state directly if they’re manually applying changes; be warned that using --fake runs the risk of putting the migration state table into a state where manual recovery will be needed to make migrations run correctly.

# --fake-initial¶
# Allows Django to skip an app’s initial migration if all database tables with the names of all models created by all CreateModel operations in that migration already exist. This option is intended for use when first running migrations against a database that preexisted the use of migrations. This option does not, however, check for matching database schema beyond matching table names and so is only safe to use if you are confident that your existing schema matches what is recorded in your initial migration.
