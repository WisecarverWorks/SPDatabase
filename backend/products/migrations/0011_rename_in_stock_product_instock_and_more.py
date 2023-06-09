# Generated by Django 4.1.7 on 2023-03-29 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_name_alter_product_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='in_stock',
            new_name='inStock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='imageURL',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
