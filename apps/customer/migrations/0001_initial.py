# Generated by Django 4.1.5 on 2023-02-06 18:11

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address_1', models.CharField(blank=True, max_length=255, null=True)),
                ('address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('country_code', models.CharField(blank=True, max_length=255, null=True)),
                ('province', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('metadata', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('iso_2', models.CharField(max_length=255, unique=True)),
                ('iso_3', models.CharField(max_length=255)),
                ('num_code', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('display_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('email', models.EmailField(help_text='Email of the customer, must be unique.', max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('first_name', models.CharField(blank=True, help_text='First name of the customer, not required.', max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, help_text='Last name of the customer, not required.', max_length=255, null=True)),
                ('phone', models.CharField(blank=True, help_text='Phone number of the customer, not required.', max_length=255, null=True)),
                ('has_account', models.BooleanField(default=False, help_text='Indicates whether the customer has an account or not.')),
                ('password_hash', models.CharField(blank=True, help_text='Hashed password of the customer, not required.', max_length=255, null=True)),
                ('metadata', models.JSONField(blank=True, help_text='Metadata related to the customer, not required.', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('metadata', models.JSONField(null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('tax_rate', models.FloatField()),
                ('tax_code', models.CharField(max_length=100, null=True)),
                ('gift_cards_taxable', models.BooleanField(default=True)),
                ('automatic_taxes', models.BooleanField(default=True)),
                ('metadata', models.JSONField(null=True)),
                ('includes_tax', models.BooleanField(default=False)),
                ('countries', models.ManyToManyField(related_name='+', to='customer.country')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
