# Generated by Django 4.2.5 on 2023-11-26 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0002_rename_endereco_funcionario_funcao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcionario',
            options={'ordering': ['nome'], 'verbose_name': 'Funcionário', 'verbose_name_plural': 'Funcionários'},
        ),
    ]