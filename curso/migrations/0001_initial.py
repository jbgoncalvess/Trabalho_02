# Generated by Django 4.2.5 on 2023-11-27 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disciplina', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do curso', max_length=50, verbose_name='Nome')),
                ('disciplinas', models.ManyToManyField(blank=True, related_name='cursos', to='disciplina.disciplina')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['nome'],
            },
        ),
    ]
