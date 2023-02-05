# Generated by Django 4.1.5 on 2023-02-04 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('customer', '0002_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customergroup',
            name='price_lists',
            field=models.ManyToManyField(to='product.pricelist'),
        ),
        migrations.AddField(
            model_name='customer',
            name='billing_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='customer.address'),
        ),
        migrations.AddField(
            model_name='customer',
            name='groups',
            field=models.ManyToManyField(related_name='+', to='customer.customergroup'),
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='order.order'),
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='customer.region'),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='customer.country'),
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='customer.customer'),
        ),
    ]