# Generated by Django 3.0.4 on 2020-06-29 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_card_fraud_app', '0012_auto_20200628_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction_details',
            name='last_transaction',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]