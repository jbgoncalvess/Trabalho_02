# Generated by Django 4.2.5 on 2023-11-27 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0003_alter_disciplina_options_alter_disciplina_alunos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='curso',
        ),
    ]
