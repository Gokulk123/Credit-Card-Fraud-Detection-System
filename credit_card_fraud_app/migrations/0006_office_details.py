# Generated by Django 3.0.4 on 2020-04-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_card_fraud_app', '0005_complaints'),
    ]

    operations = [
        migrations.CreateModel(
            name='office_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
