# Generated by Django 4.1.7 on 2023-08-06 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0013_product_height_product_length_product_weight_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="origin_country",
        ),
        migrations.AddField(
            model_name="image",
            name="file",
            field=models.ImageField(blank=True, null=True, upload_to="product/images/"),
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="product.productcategory",
            ),
        ),
    ]
