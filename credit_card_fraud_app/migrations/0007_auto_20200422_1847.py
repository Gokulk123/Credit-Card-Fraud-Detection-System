# Generated by Django 3.0.4 on 2020-04-22 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credit_card_fraud_app', '0006_office_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='office_details',
            new_name='bank_details',
        ),
    ]