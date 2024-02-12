# Generated by Django 5.0.2 on 2024-02-10 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=100)),
                ('stock_status', models.FloatField()),
                ('available_stock', models.FloatField()),
            ],
        ),
    ]