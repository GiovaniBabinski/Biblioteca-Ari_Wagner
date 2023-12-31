# Generated by Django 4.2.4 on 2023-09-04 03:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0029_alter_emprestimos_avaliacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_emprestado_anonimo', models.CharField(blank=True, max_length=30)),
                ('data_emprestimo', models.DateField(blank=True)),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('avaliacao', models.CharField(blank=True, choices=[('P', 'Péssimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Otimo')], max_length=1)),
            ],
            options={
                'verbose_name': 'Emprestimo',
            },
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(default=datetime.date(2023, 9, 4)),
        ),
        migrations.DeleteModel(
            name='Emprestimos',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.livros'),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='nome_emprestado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
        ),
    ]
