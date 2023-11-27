# Generated by Django 4.2.5 on 2023-09-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do produto', max_length=50, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, help_text='Preço do produto', max_digits=6, verbose_name='Preço')),
                ('fornecedor', models.CharField(help_text='Nome do fornecedor', max_length=50, verbose_name='Fornecedor')),
                ('quantidade', models.DecimalField(decimal_places=2, help_text='Quantidade em estoque do produto', max_digits=5, verbose_name='Quantidade')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]