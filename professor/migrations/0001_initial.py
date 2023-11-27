# Generated by Django 4.2.5 on 2023-11-27 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do professor', max_length=50, verbose_name='Nome')),
                ('siape', models.DecimalField(decimal_places=0, help_text='Número do siape', max_digits=20, unique=True, verbose_name='Siape')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
                'ordering': ['nome'],
            },
        ),
    ]
