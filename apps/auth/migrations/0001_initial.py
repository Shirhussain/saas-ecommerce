# Generated by Django 4.1.5 on 2023-02-04 18:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oauth',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('display_name', models.CharField(max_length=255)),
                ('application_name', models.CharField(max_length=255, unique=True)),
                ('install_url', models.CharField(max_length=255, null=True)),
                ('uninstall_url', models.CharField(max_length=255, null=True)),
                ('data', models.JSONField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PublishableApiKey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=100, null=True)),
                ('revoked_by', models.CharField(max_length=100, null=True)),
                ('revoked_at', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PublishableApiKeySalesChannel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('sales_channel_id', models.CharField(max_length=100, unique=True)),
                ('publishable_key_id', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]