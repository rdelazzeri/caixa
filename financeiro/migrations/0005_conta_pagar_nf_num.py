# Generated by Django 3.2.7 on 2022-02-08 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0004_auto_20220204_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta_pagar',
            name='nf_num',
            field=models.IntegerField(default=0),
        ),
    ]
