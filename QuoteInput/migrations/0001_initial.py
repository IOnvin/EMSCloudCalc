# Generated by Django 2.2.6 on 2020-06-09 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteInputModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_name', models.CharField(max_length=56, null=True)),
                ('Opportunity_ID', models.CharField(max_length=120)),
                ('customer_name', models.CharField(max_length=120)),
                ('opp_url', models.URLField(blank=True, help_text='copy and paste SFDC Opportunity URL', null=True)),
                ('lead_name', models.CharField(choices=[('Arlene Branham', 'Arlene Branham'), ('John Smith', 'John Smith'), ('Sharron Harman', 'Sharron Harman'), ('Harry Anderson', 'Harry Anderson')], max_length=56)),
                ('term_type', models.CharField(choices=[('Cloud Subscription', 'Cloud Subscription'), ('Cloud Perpetual', 'Cloud Perpetual'), ('SaaS', 'SaaS')], max_length=56)),
                ('Leading_Product', models.CharField(choices=[('OpenText ContentSuite', 'OpenText ContentSuite'), ('OpenText Experience Suite', 'OpenText Experience Suite'), ('OpenText Process Suite', 'OpenText Process Suite'), ('OpenText Information Exchange Suite', 'OpenText Information Exchange Suite'), ('OpenText Discovery Suite', 'OpenText Discovery Suite'), ('OpenText Suite for SAP', 'OpenText Suite for SAP'), ('OpenText Suite for Oracle', 'OpenText Suite for Oracle'), ('OpenText Suite for Microsoft', 'OpenText Suite for Microsoft'), ('OpenText Appworks', 'OpenText Appworks'), ('OpenText Cloud', 'OpenText Cloud')], max_length=120)),
                ('penalties', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=56)),
                ('managed_services', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=56, null=True)),
                ('managed_services_rep', models.CharField(choices=[('M1', 'CDS Rep 1'), ('M2', 'CDS Rep 2'), ('M3', 'CDS Rep 3'), ('M4', 'CDS Rep 4'), ('M5', 'CDS Rep 5')], max_length=56, null=True)),
                ('local_Currency', models.CharField(choices=[('USD', 'USD'), ('AED', 'AED'), ('AFN', 'AFN'), ('ALL', 'ALL'), ('AMD', 'AMD'), ('ANG', 'ANG'), ('AOA', 'AOA'), ('ARS', 'ARS'), ('AUD', 'AUD'), ('AZN', 'AZN'), ('BAM', 'BAM'), ('BBD', 'BBD'), ('BDT', 'BDT'), ('BGN', 'BGN'), ('BHD', 'BHD'), ('BIF', 'BIF'), ('BMD', 'BMD'), ('BND', 'BND'), ('BOB', 'BOB'), ('BRL', 'BRL'), ('BSD', 'BSD'), ('BTN', 'BTN'), ('BWP', 'BWP'), ('BZD', 'BZD'), ('CAD', 'CAD'), ('CDF', 'CDF'), ('CHF', 'CHF'), ('CLP', 'CLP'), ('CNH', 'CNH'), ('CNY', 'CNY'), ('COP', 'COP'), ('CRC', 'CRC'), ('CVE', 'CVE'), ('CYP', 'CYP'), ('CZK', 'CZK'), ('DJF', 'DJF'), ('DKK', 'DKK'), ('DOP', 'DOP'), ('DZD', 'DZD'), ('EEK', 'EEK'), ('EGP', 'EGP'), ('ETB', 'ETB'), ('EUR', 'EUR'), ('FJD', 'FJD'), ('GBP', 'GBP'), ('GEL', 'GEL'), ('GHS', 'GHS'), ('GIP', 'GIP'), ('GMD', 'GMD'), ('GNF', 'GNF'), ('GTQ', 'GTQ'), ('GYD', 'GYD'), ('HKD', 'HKD'), ('HNL', 'HNL'), ('HRK', 'HRK'), ('HTG', 'HTG'), ('HUF', 'HUF'), ('IDR', 'IDR'), ('ILS', 'ILS'), ('INR', 'INR'), ('IRR', 'IRR'), ('ISK', 'ISK'), ('JMD', 'JMD'), ('JOD', 'JOD'), ('JPY', 'JPY'), ('KES', 'KES'), ('KGS', 'KGS'), ('KHR', 'KHR'), ('KMF', 'KMF'), ('KRW', 'KRW'), ('KWD', 'KWD'), ('KYD', 'KYD'), ('KZT', 'KZT'), ('LAK', 'LAK'), ('LBP', 'LBP'), ('LKR', 'LKR'), ('LSL', 'LSL'), ('LTL', 'LTL'), ('LVL', 'LVL'), ('MAD', 'MAD'), ('MDL', 'MDL'), ('MGA', 'MGA'), ('MKD', 'MKD'), ('MMK', 'MMK'), ('MNT', 'MNT'), ('MOP', 'MOP'), ('MRO', 'MRO'), ('MTL', 'MTL'), ('MUR', 'MUR'), ('MVR', 'MVR'), ('MWK', 'MWK'), ('MXN', 'MXN'), ('MYR', 'MYR'), ('MZN', 'MZN'), ('NAD', 'NAD'), ('NGN', 'NGN'), ('NIO', 'NIO'), ('NOK', 'NOK'), ('NPR', 'NPR'), ('NZD', 'NZD'), ('OMR', 'OMR'), ('PAB', 'PAB'), ('PEN', 'PEN'), ('PGK', 'PGK'), ('PHP', 'PHP'), ('PKR', 'PKR'), ('PLN', 'PLN'), ('PYG', 'PYG'), ('QAR', 'QAR'), ('RON', 'RON'), ('RSD', 'RSD'), ('RUB', 'RUB'), ('RWF', 'RWF'), ('SAR', 'SAR'), ('SBD', 'SBD'), ('SCR', 'SCR'), ('SDG', 'SDG'), ('SEK', 'SEK'), ('SGD', 'SGD'), ('SIT', 'SIT'), ('SKK', 'SKK'), ('SLL', 'SLL'), ('SRD', 'SRD'), ('STD', 'STD'), ('SVC', 'SVC'), ('SYP', 'SYP'), ('SZL', 'SZL'), ('THB', 'THB'), ('TJS', 'TJS'), ('TND', 'TND'), ('TOP', 'TOP'), ('TRY', 'TRY'), ('TTD', 'TTD'), ('TWD', 'TWD'), ('TZS', 'TZS'), ('UAH', 'UAH'), ('UGX', 'UGX'), ('UYU', 'UYU'), ('UZS', 'UZS'), ('VEF', 'VEF'), ('VND', 'VND'), ('VUV', 'VUV'), ('WST', 'WST'), ('XAF', 'XAF'), ('XCD', 'XCD'), ('XOF', 'XOF'), ('XPF', 'XPF'), ('YER', 'YER'), ('ZAR', 'ZAR'), ('ZMW', 'ZMW')], max_length=56, null=True)),
                ('perpetualSoftwareOTDirectDiscount', models.FloatField(default=10)),
                ('subscriptionSoftwareOTDirectDiscount', models.FloatField(default=85)),
                ('perpetualSoftwareThirdPartyDiscount', models.FloatField(default=5)),
                ('subscriptionSoftwareThirdPartyDiscount', models.FloatField(default=30)),
            ],
        ),
    ]