# Generated by Django 3.0.4 on 2020-04-23 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_card_fraud_app', '0007_auto_20200422_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account_details',
            name='account_balance',
        ),
        migrations.RemoveField(
            model_name='account_details',
            name='account_no',
        ),
        migrations.RemoveField(
            model_name='account_details',
            name='card_no',
        ),
        migrations.RemoveField(
            model_name='account_details',
            name='cvv_code',
        ),
        migrations.RemoveField(
            model_name='account_details',
            name='exp_date',
        ),
        migrations.RemoveField(
            model_name='account_details',
            name='status',
        ),
        migrations.AddField(
            model_name='account_details',
            name='acct_num',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='account_details',
            name='branch',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='account_details',
            name='card_num',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='account_details',
            name='customer_id',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='account_details',
            name='customer_name',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='account_details',
            name='date',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='account_details',
            name='email',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='account_details',
            name='ifsc',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='account_details',
            name='phone',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='account_details',
            name='pin',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='account_details',
            name='place',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
