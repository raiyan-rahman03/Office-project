# Generated by Django 3.2.3 on 2024-03-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teebay_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='rental_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='rental_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
