# Generated by Django 3.2.7 on 2022-01-24 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0006_auto_20220119_1643'),
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta_pagar',
            name='vencimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conta_pagar',
            name='banco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financeiro.banco'),
        ),
        migrations.AlterField(
            model_name='conta_pagar',
            name='conta_caixa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financeiro.plano_contas'),
        ),
        migrations.AlterField(
            model_name='conta_pagar',
            name='data_emissao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conta_pagar',
            name='data_pagamento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conta_pagar',
            name='entrada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entradas.nf_entrada'),
        ),
        migrations.AlterField(
            model_name='conta_pagar',
            name='origem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financeiro.origem'),
        ),
        migrations.AlterField(
            model_name='conta_pagar',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financeiro.status'),
        ),
        migrations.AlterField(
            model_name='conta_receber',
            name='banco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financeiro.banco'),
        ),
        migrations.AlterField(
            model_name='conta_receber',
            name='conta_caixa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financeiro.plano_contas'),
        ),
        migrations.AlterField(
            model_name='conta_receber',
            name='data_pagamento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conta_receber',
            name='origem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financeiro.origem'),
        ),
        migrations.AlterField(
            model_name='conta_receber',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='financeiro.status'),
        ),
    ]
