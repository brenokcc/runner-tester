# Generated by Django 4.2.6 on 2024-05-25 21:43

from django.db import migrations, models
import django.db.models.deletion
import slth
import slth.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Esfera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Esfera',
                'verbose_name_plural': 'Esferas',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', slth.db.models.CharField(max_length=255, verbose_name='Sigla')),
                ('nome', slth.db.models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'icon': 'map',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='InstrumentoAvaliativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(max_length=255, verbose_name='Nome')),
                ('data_inicio', models.DateField(verbose_name='Início')),
                ('data_termino', models.DateField(verbose_name='Término')),
                ('instrucoes', slth.db.models.TextField(blank=True, null=True, verbose_name='Instruções')),
            ],
            options={
                'verbose_name': 'Instrumento Avaliativo',
                'verbose_name_plural': 'Instrumentos Avaliativos',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='NivelEnsino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Nível de Ensino',
                'verbose_name_plural': 'Níveis de Ensino',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='OpcaoResposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', slth.db.models.CharField(max_length=255, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Opção de Resposta',
                'verbose_name_plural': 'Opções de Resposta',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', slth.db.models.TextField(verbose_name='Enunciado')),
                ('tipo_resposta', slth.db.models.IntegerField(choices=[(1, 'Texto curso'), (2, 'Texto longo'), (3, 'Data'), (4, 'Decimal'), (5, 'Inteiro'), (6, 'Escolha'), (7, 'Múltipla Escolha')], verbose_name='Tipo da Resposta')),
                ('resposta_obrigatoria', models.BooleanField(blank=True, verbose_name='Resposta Obrigatória')),
                ('instrumento_avaliativo', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.instrumentoavaliativo', verbose_name='Instrumento Avaliativo')),
                ('opcoes', slth.db.models.OneToManyField(to='api.opcaoresposta', verbose_name='Opções de Resposta')),
            ],
            options={
                'verbose_name': 'Pergunta',
                'verbose_name_plural': 'Perguntas',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', slth.db.models.ImageField(blank=True, null=True, upload_to='pessoas_fisicas', verbose_name='Foto')),
                ('cpf', slth.db.models.CharField(max_length=255, verbose_name='CPF')),
                ('nome', slth.db.models.CharField(max_length=255, verbose_name='Nome')),
                ('nome_social', slth.db.models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome Social')),
                ('telefone', slth.db.models.CharField(max_length=255, verbose_name='Telefone')),
                ('email', slth.db.models.CharField(max_length=255, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Pessoa Física',
                'verbose_name_plural': 'Pessoas Físicas',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='Poder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Poder',
                'verbose_name_plural': 'Poderes',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='SituacaoEscolaridade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Situação de Escolaridade',
                'verbose_name_plural': 'Situações de Escolaridade',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='TipoOrgao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Tipo de Orgão',
                'verbose_name_plural': 'Tipos de Orgãos',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='TipoRedeSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Tipo de Rede Social',
                'verbose_name_plural': 'Tipos de Rede Social',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='RedeSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informacao', slth.db.models.CharField(max_length=255, verbose_name='Informação')),
                ('pessoa_fisica', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pessoafisica', verbose_name='Pessoa Física')),
                ('tipo', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tiporedesocial', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Rede Social',
                'verbose_name_plural': 'Redes Sociais',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrumento_avaliativo', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.instrumentoavaliativo', verbose_name='Instrumento Avaliativo')),
                ('respondente', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pessoafisica', verbose_name='Respondente')),
            ],
            options={
                'verbose_name': 'Questionário',
                'verbose_name_plural': 'Questionários',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='PerguntaQuestionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', slth.db.models.CharField(blank=True, max_length=255, null=True, verbose_name='Resposta')),
                ('pergunta', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pergunta', verbose_name='Pergunta')),
                ('questionario', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.questionario', verbose_name='Questionário')),
            ],
            options={
                'verbose_name': 'Pergunta de Questionário',
                'verbose_name_plural': 'Perguntas de Questionário',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', slth.db.models.CharField(max_length=255, verbose_name='Sigla')),
                ('nome', slth.db.models.CharField(max_length=255, verbose_name='Nome')),
                ('cnpj', slth.db.models.CharField(max_length=255, verbose_name='CNPJ')),
                ('esfera', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.esfera', verbose_name='Esfera')),
                ('poder', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.poder', verbose_name='Poder')),
                ('tipo', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipoorgao', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Orgão',
                'verbose_name_plural': 'Orgãos',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(max_length=255, verbose_name='Nome')),
                ('latitude', slth.db.models.CharField(blank=True, max_length=255, null=True, verbose_name='Latitude')),
                ('longitude', slth.db.models.CharField(blank=True, max_length=255, null=True, verbose_name='Longitude')),
                ('estado', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.estado', verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Município',
                'verbose_name_plural': 'Municípios',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.AddField(
            model_name='instrumentoavaliativo',
            name='responsavel',
            field=slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pessoafisica', verbose_name='Responsável'),
        ),
        migrations.CreateModel(
            name='Escolaridade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituicao', slth.db.models.CharField(blank=True, max_length=255, null=True, verbose_name='Instituição')),
                ('curso', slth.db.models.CharField(blank=True, max_length=255, null=True, verbose_name='Curso')),
                ('nivel_ensino', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.nivelensino', verbose_name='Nível de Ensino')),
                ('pessoa_fisica', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pessoafisica', verbose_name='Pessoa Física')),
                ('situacao', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.situacaoescolaridade', verbose_name='Situação')),
            ],
            options={
                'verbose_name': 'Escolaridade',
                'verbose_name_plural': 'Escolaridades',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
    ]
