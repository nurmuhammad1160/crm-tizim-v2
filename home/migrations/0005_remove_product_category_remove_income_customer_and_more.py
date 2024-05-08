# Generated by Django 5.0 on 2024-04-30 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_category_table_alter_income_table_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='income',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='income',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Income',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Tipe',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
