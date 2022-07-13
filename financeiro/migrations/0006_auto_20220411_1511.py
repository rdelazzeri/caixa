# Generated by Django 3.2.7 on 2022-04-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0005_conta_pagar_nf_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='plano_contas',
            name='banco',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='plano_contas',
            name='cod_cyber',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='plano_contas',
            name='nivel',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='plano_contas',
            name='tipo',
            field=models.CharField(blank=True, choices=[('CR', 'CONTAS A RECEBER'), ('CP', 'CONTAS A PAGAR')], max_length=2, null=True),
        ),
    ]
