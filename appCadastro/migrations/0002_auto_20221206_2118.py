# Generated by Django 3.0 on 2022-12-07 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao_produto',
            field=models.TextField(blank=True),
        ),
    ]
