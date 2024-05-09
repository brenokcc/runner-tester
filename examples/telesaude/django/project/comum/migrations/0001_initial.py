# Generated by Django 4.2.6 on 2024-05-07 06:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
import slth
import slth.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('slth', '0006_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaTematica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(max_length=60, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('ativo_sincrona', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Área Temática',
                'verbose_name_plural': 'Áreas Temáticas',
                'ordering': ['nome'],
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='CategoriaProfissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_familia_cbo', slth.db.models.CharField(max_length=4, unique=True, verbose_name='Código')),
                ('nome', slth.db.models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='CIAP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', slth.db.models.CharField(max_length=6, unique=True, verbose_name='Código')),
                ('doenca', slth.db.models.CharField(max_length=100, verbose_name='Doença')),
            ],
            options={
                'verbose_name': 'CIAP',
                'verbose_name_plural': 'CIAPs',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='CID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', slth.db.models.CharField(max_length=6, unique=True, verbose_name='Código')),
                ('doenca', slth.db.models.CharField(max_length=250, verbose_name='Doença')),
            ],
            options={
                'verbose_name': 'CID',
                'verbose_name_plural': 'CIDs',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_cbo', slth.db.models.CharField(max_length=6, unique=True, verbose_name='Código')),
                ('nome', slth.db.models.CharField(max_length=150)),
                ('categoria', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comum.categoriaprofissional')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='EstabelecimentoSaude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_cnes', slth.db.models.CharField(max_length=12, unique=True, verbose_name='CNES')),
                ('nome', slth.db.models.CharField(max_length=100)),
                ('logradouro', slth.db.models.CharField(max_length=120, null=True)),
                ('numero', slth.db.models.CharField(max_length=10, null=True)),
                ('bairro', slth.db.models.CharField(max_length=40, null=True)),
                ('cep', slth.db.models.CharField(max_length=10, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='FluxoSolicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
                ('comentario', slth.db.models.TextField(blank=True)),
                ('encaminhamento', slth.db.models.TextField(blank=True, null=True)),
                ('conduta', slth.db.models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', slth.db.models.CharField(max_length=6, unique=True)),
                ('nome', slth.db.models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='NivelFormacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(max_length=25, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='ProfissionalSaude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_profissional', slth.db.models.CharField(blank=True, max_length=30, verbose_name='Registro Profissional')),
                ('registro_especialista', slth.db.models.CharField(blank=True, max_length=30, null=True, verbose_name='Registro Especialista')),
                ('programa_provab', models.BooleanField(default=False)),
                ('programa_mais_medico', models.BooleanField(default=False)),
                ('formacao', slth.db.models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profissional', to='comum.nivelformacao')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='ProfissionalVinculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residente', models.BooleanField(default=False)),
                ('perceptor', models.BooleanField(default=False)),
                ('ativo', models.BooleanField(default=False)),
                ('estabelecimento', slth.db.models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vinculos', to='comum.estabelecimentosaude')),
                ('profissao', slth.db.models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vinculos', to='comum.especialidade')),
                ('profissional', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vinculos', to='comum.profissionalsaude')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='StatusSolicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', slth.db.models.CharField(choices=[('rascunho', 'Rascunho'), ('nova', 'Nova'), ('encaminhada', 'Encaminhada'), ('aceita', 'Aceita'), ('devolvida', 'Devolvida'), ('respondida', 'Respondida'), ('remarcada', 'Devolvida ao Telerregulador'), ('finalizada', 'Finalizada'), ('cancelada', 'Cancelada'), ('reagendada', 'Reagendamento'), ('agendada', 'Agendada'), ('realizada', 'Realizada'), ('nao_realizada', 'Não Realizada')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='TipoEnfoqueResposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(max_length=150)),
                ('enfoque_principal', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Enfoque de Solicitação de Resposta',
                'verbose_name_plural': 'Enfoques de Solicitação de Resposta',
                'ordering': ['nome'],
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='TipoSolicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(choices=[(1, 'Síncrona (Vídeo)'), (2, 'Assíncrona (Texto)')], max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='UnidadeFederativa',
            fields=[
                ('codigo', slth.db.models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('sigla', slth.db.models.CharField(max_length=2, unique=True)),
                ('nome', slth.db.models.CharField(max_length=60, unique=True)),
            ],
            options={
                'ordering': ['nome'],
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', slth.db.models.CharField(max_length=80)),
                ('nome_social', slth.db.models.CharField(blank=True, max_length=80, null=True)),
                ('cpf', slth.db.models.CharField(max_length=14, unique=True)),
                ('telefone', slth.db.models.CharField(blank=True, max_length=15, null=True)),
                ('endereco', slth.db.models.CharField(blank=True, max_length=255, null=True)),
                ('numero', slth.db.models.CharField(blank=True, max_length=255, null=True)),
                ('cep', slth.db.models.CharField(blank=True, max_length=255, null=True)),
                ('bairro', slth.db.models.CharField(blank=True, max_length=255, null=True)),
                ('complemento', slth.db.models.CharField(blank=True, max_length=150, null=True)),
                ('data_nascimento', models.DateField(null=True)),
                ('cns', slth.db.models.CharField(max_length=15, null=True)),
                ('municipio', slth.db.models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='comum.municipio')),
                ('perfil', slth.db.models.ManyToManyField(related_name='usuario', to='comum.perfil')),
                ('sexo', slth.db.models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='usuarios', to='comum.sexo')),
                ('user', slth.db.models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='usuario', to='slth.user')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(blank=True)),
                ('assunto', slth.db.models.CharField(max_length=200)),
                ('duvida', slth.db.models.CharField(max_length=2000)),
                ('duracao', models.DurationField(default=datetime.timedelta(0), null=True)),
                ('atraso', models.BooleanField(default=False, null=True)),
                ('sugestao_sincrona', slth.db.models.CharField(max_length=150, null=True)),
                ('agendado_para', models.DateTimeField(null=True)),
                ('finalizado_em', models.DateTimeField(null=True)),
                ('qtd_acessos', slth.db.models.IntegerField(default=0)),
                ('area_tematica', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacoes', to='comum.areatematica')),
                ('ciap', slth.db.models.ManyToManyField(related_name='ciaps', to='comum.ciap')),
                ('cid', slth.db.models.ManyToManyField(related_name='cids', to='comum.cid')),
                ('enfoque_solicitacao', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacoes', to='comum.tipoenfoqueresposta')),
                ('motivadora', slth.db.models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='duvida_filha', to='comum.solicitacao')),
                ('paciente', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='solicitacoes_paciente', to='comum.usuario')),
                ('tipo_solicitacao', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacoes', to='comum.tiposolicitacao')),
                ('ultimo_fluxo', slth.db.models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ultimo_fluxo_solicitacao', to='comum.fluxosolicitacao')),
                ('vinculo', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacoes', to='comum.profissionalvinculo')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='ProfissionalSaudeGestorMunicipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gestor_municipio', to='comum.municipio')),
                ('profissional_saude', slth.db.models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='gestor_municipio', to='comum.profissionalsaude')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='ProfissionalSaudeEspecialista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilitado_iatae', models.BooleanField(default=False)),
                ('receber_tcs', models.BooleanField(default=True)),
                ('area_tematica', slth.db.models.ManyToManyField(related_name='especialista', to='comum.areatematica')),
                ('profissional_saude', slth.db.models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='especialista', to='comum.profissionalsaude')),
                ('tipo_solicitacao', slth.db.models.ManyToManyField(related_name='especialista', to='comum.tiposolicitacao')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.AddField(
            model_name='profissionalsaude',
            name='usuario',
            field=slth.db.models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='profissional_saude', to='comum.usuario'),
        ),
        migrations.AddField(
            model_name='municipio',
            name='estado',
            field=slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comum.unidadefederativa'),
        ),
        migrations.CreateModel(
            name='MotivoEncerramentoConferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', slth.db.models.CharField(choices=[('ausencia_solicitante', 'Ausência do Solicitante'), ('ausencia_paciente', 'Ausência do Paciente'), ('ausencia_ambos', 'Ausência do Solicitante e Paciente'), ('outro', 'Outro')], max_length=40)),
                ('consideracoes', slth.db.models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
                ('profissional', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motivos_realizacao', to='comum.profissionalsaude')),
                ('solicitacao', slth.db.models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='motivo_realizacao', to='comum.solicitacao')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='HistoricoAlteracaoProfissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acao', slth.db.models.CharField(choices=[('criado', 'Cadastro Realizado'), ('modificado', 'Dados Alterados'), ('aceite', 'Cadastro Aceito'), ('vinculo_modificado', 'Alteração de Vínculos')], max_length=25)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('profissional', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historico_alteracoes', to='comum.profissionalsaude')),
                ('usuario', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historico_alteracoes', to='comum.usuario')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.AddField(
            model_name='fluxosolicitacao',
            name='profissional_destino',
            field=slth.db.models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fluxos_profissional_destino', to='comum.profissionalsaude'),
        ),
        migrations.AddField(
            model_name='fluxosolicitacao',
            name='responsavel',
            field=slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fluxos_responsavel', to='comum.profissionalsaude'),
        ),
        migrations.AddField(
            model_name='fluxosolicitacao',
            name='solicitacao',
            field=slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fluxos', to='comum.solicitacao'),
        ),
        migrations.AddField(
            model_name='fluxosolicitacao',
            name='status_novo',
            field=slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fluxos_novos', to='comum.statussolicitacao'),
        ),
        migrations.AddField(
            model_name='estabelecimentosaude',
            name='municipio',
            field=slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estabelecimentos', to='comum.municipio'),
        ),
        migrations.CreateModel(
            name='CertificadoDigital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', slth.db.models.FileField(upload_to='certificados_digitais', verbose_name='Arquivo')),
                ('descricao', slth.db.models.CharField(max_length=255, verbose_name='Descrição')),
                ('validade', models.DateField(verbose_name='Validade')),
                ('user', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slth.user', verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Certificado Digital',
                'verbose_name_plural': 'Certificados Digitais',
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='AvaliacaoSolicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satisfacao', slth.db.models.IntegerField(choices=[(1, 'Muito Satisfeito'), (2, 'Satisfeito'), (3, 'Indiferente'), (4, 'Insatisfeito'), (5, 'Muito Insatisfeito')])),
                ('respondeu_duvida', slth.db.models.IntegerField(choices=[(1, 'Sim'), (2, 'Parcialmente'), (3, 'Não')])),
                ('evitou_encaminhamento', slth.db.models.IntegerField(choices=[(1, 'Sim, evitou'), (2, 'Não, pois ainda será necessário referenciá-lo (encaminhá-lo)'), (3, 'Não, pois não era minha intenção referenciá-lo antes da teleconsulta'), (4, 'Não, por outros motivos')])),
                ('mudou_conduta', slth.db.models.IntegerField(choices=[(1, 'Sim'), (2, 'Não, pois eu já seguia a conduta/abordagem sugerida'), (3, 'Não, pois não concordo com a reposta'), (4, 'Não, pois não há como seguir a conduta sugerida em nosso contexto'), (5, 'Não, por outros motivos')])),
                ('recomendaria', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=None)),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
                ('solicitacao', slth.db.models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='avaliacao', to='comum.solicitacao')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='AnexoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', slth.db.models.FileField(max_length=200, upload_to='imagens_reconhecimento')),
                ('documento', slth.db.models.FileField(max_length=200, null=True, upload_to='documento')),
                ('usuario', slth.db.models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='foto_confirmacao', to='comum.usuario')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='AnexoSolicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', slth.db.models.FileField(max_length=200, upload_to='anexos_teleconsuta')),
                ('autor', slth.db.models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anexos_solicitacoes', to='comum.usuario')),
                ('solicitacao', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anexos', to='comum.solicitacao')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
        migrations.CreateModel(
            name='ProfissionalSaudeRegulador',
            fields=[
                ('profissional_saude', slth.db.models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='regulador', serialize=False, to='comum.profissionalsaude')),
                ('area_tematica', slth.db.models.ManyToManyField(to='comum.areatematica')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, slth.ModelMixin),
        ),
    ]