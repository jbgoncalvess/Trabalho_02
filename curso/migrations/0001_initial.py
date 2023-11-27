# Generated by Django 4.2.5 on 2023-11-26 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('universidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do curso', max_length=50, verbose_name='Nome')),
                ('universidade', models.ForeignKey(help_text='Nome da universidade', on_delete=django.db.models.deletion.CASCADE, to='universidade.universidade', verbose_name='Universidade')),
            ],
        ),
    ]