# Generated by Django 4.0.6 on 2022-07-13 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0006_alter_cc_banco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='desc',
            new_name='nome',
        ),
    ]
