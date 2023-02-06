# Generated by Django 4.1.5 on 2023-02-06 18:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('symbol', models.CharField(max_length=255)),
                ('symbol_native', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('includes_tax', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IdempotencyKey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('idempotency_key', models.CharField(max_length=255, unique=True)),
                ('locked_at', models.DateTimeField(blank=True, null=True)),
                ('request_method', models.CharField(blank=True, max_length=255, null=True)),
                ('request_params', models.JSONField(blank=True, null=True)),
                ('request_path', models.CharField(blank=True, max_length=255, null=True)),
                ('response_code', models.IntegerField(blank=True, null=True)),
                ('response_body', models.JSONField(blank=True, null=True)),
                ('recovery_point', models.CharField(default='started', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('amount', models.FloatField()),
                ('amount_refunded', models.FloatField(default=0)),
                ('provider_id', models.CharField(max_length=255)),
                ('data', models.JSONField()),
                ('captured_at', models.DateTimeField(null=True)),
                ('canceled_at', models.DateTimeField(null=True)),
                ('metadata', models.JSONField(null=True)),
                ('idempotency_key', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentCollection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('type', models.CharField(choices=[('not_paid', 'NOT_PAID'), ('awaiting', 'AWAITING'), ('authorized', 'AUTHORIZED'), ('partially_authorized', 'PARTIALLY_AUTHORIZED'), ('canceled', 'CANCELED')], max_length=20)),
                ('status', models.CharField(choices=[('order_edit', 'ORDER_EDIT')], max_length=20)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.FloatField()),
                ('authorized_amount', models.FloatField(blank=True, null=True)),
                ('metadata', models.JSONField()),
                ('created_by', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentProvider',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_installed', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentSession',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('provider_id', models.CharField(max_length=100)),
                ('is_selected', models.BooleanField(null=True)),
                ('is_initiated', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('authorized', 'AUTHORIZED'), ('pending', 'PENDING'), ('requires_more', 'REQUIRES_MORE'), ('error', 'ERROR'), ('canceled', 'CANCELED')], max_length=100)),
                ('data', models.JSONField()),
                ('idempotency_key', models.CharField(max_length=100, null=True)),
                ('amount', models.FloatField(null=True)),
                ('payment_authorized_at', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('amount', models.IntegerField()),
                ('note', models.TextField(null=True)),
                ('reason', models.CharField(choices=[('discount', 'DISCOUNT'), ('return', 'RETURN'), ('swap', 'SWAP'), ('claim', 'CLAIM'), ('other', 'OTHER')], max_length=16)),
                ('metadata', models.JSONField(null=True)),
                ('idempotency_key', models.CharField(max_length=255, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='order.order')),
                ('payment', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='payment.payment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
