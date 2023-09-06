# Generated by Django 4.2.5 on 2023-09-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=8, verbose_name='Placa')),
                ('marca', models.CharField(max_length=15, verbose_name='Marca')),
                ('veiculo', models.CharField(max_length=30, verbose_name='Veículo')),
                ('km_troca_oleo', models.DecimalField(decimal_places=4, max_digits=8, verbose_name='km_Troca_Oleo')),
            ],
        ),
    ]