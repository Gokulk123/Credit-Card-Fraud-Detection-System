# Generated by Django 3.0.4 on 2020-04-07 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_card_fraud_app', '0004_security_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_id', models.CharField(max_length=100)),
                ('userid', models.CharField(max_length=100)),
                ('card_no', models.CharField(max_length=100)),
                ('transaction_id', models.CharField(max_length=100)),
            ],
        ),
    ]
