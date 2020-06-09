# Generated by Django 2.2.6 on 2020-06-09 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoteInput', '0005_auto_20200609_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='quoteinputmodel',
            name='GCPSoleTenantNodesVCPUs96RAM624GBPerSTN',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='OSPatching',
            field=models.CharField(choices=[('Full', 'Full'), ('Partial', 'Partial')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='activeActiveDBRequired',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='additionalCloudDeliveryOpsCostsOneTimeUSD',
            field=models.FloatField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='additionalCloudDeliveryOpsCostsPcmUSD',
            field=models.FloatField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='applicationMonitoringRequiredNewRelic',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='databaseAdministrationAndTuning',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='firewall',
            field=models.CharField(choices=[('Multiple Access Points', 'Multiple Access Points'), ('Single Access Point', 'Single Access Point')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='loadBalancing',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='numberOfClientBasedVPNs',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='numberOfSiteToSiteVPNs',
            field=models.CharField(choices=[(0, 0), (1, 1)], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='problemEscalationAndResponse',
            field=models.CharField(choices=[('24x7', '24x7'), ('10x5', '10x5')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='thirdPartyAzureRemoteAccess',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='threatManagementAndSecurityScans',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='quoteinputmodel',
            name='willTheCustomerUseMPLSVPLSCircuitsToConnect',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True),
        ),
    ]
