# Generated by Django 3.0 on 2022-12-06 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_produto', models.CharField(max_length=100)),
                ('marca_produto', models.CharField(max_length=30)),
                ('descricao_produto', models.TextField()),
                ('data_cadastro', models.DateField()),
                ('preco_compra', models.FloatField()),
                ('preco_venda', models.FloatField()),
            ],
        ),
    ]