# Generated by Django 4.2.5 on 2023-11-27 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_alter_professor_options_remove_professor_disciplina'),
        ('aluno', '0002_alter_aluno_options'),
        ('disciplina', '0004_remove_disciplina_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='alunos',
            field=models.ManyToManyField(to='aluno.aluno'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professor.professor'),
        ),
    ]