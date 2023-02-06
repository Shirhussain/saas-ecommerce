# Generated by Django 4.1.5 on 2023-02-06 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0003_initial'),
        ('tax', '0001_initial'),
        ('payment', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='payment.currency'),
        ),
        migrations.AddField(
            model_name='region',
            name='fulfillment_providers',
            field=models.ManyToManyField(related_name='+', to='inventory.fulfillmentprovider'),
        ),
        migrations.AddField(
            model_name='region',
            name='payment_providers',
            field=models.ManyToManyField(related_name='+', to='payment.paymentprovider'),
        ),
        migrations.AddField(
            model_name='region',
            name='tax_provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tax.taxprovider'),
        ),
        migrations.AddField(
            model_name='region',
            name='tax_rates',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tax.taxrate'),
        ),
        migrations.AddField(
            model_name='customergroup',
            name='customers',
            field=models.ManyToManyField(related_name='+', to='customer.customer'),
        ),
    ]
