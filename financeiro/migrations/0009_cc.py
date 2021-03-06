# Generated by Django 3.2.7 on 2022-06-03 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0012_parceiro_cod_cyber'),
        ('financeiro', '0008_auto_20220422_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='CC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('desc', models.CharField(max_length=40)),
                ('credito', models.DecimalField(decimal_places=2, default=0, max_digits=13)),
                ('debito', models.DecimalField(decimal_places=2, default=0, max_digits=13)),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=13)),
                ('parceiro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro.parceiro')),
            ],
        ),
    ]
