# Generated by Django 2.1.5 on 2019-01-23 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='valores_bancoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idvalor', models.BigIntegerField()),
                ('valor_banco_brasil', models.BigIntegerField()),
                ('valor_banco_bradesco', models.BigIntegerField()),
            ],
        ),
    ]
