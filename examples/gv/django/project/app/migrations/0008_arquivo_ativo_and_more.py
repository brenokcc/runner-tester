# Generated by Django 4.2.6 on 2024-05-01 09:00

from django.db import migrations, models
import django.db.models.deletion
import slth
import slth.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_consulta_pergunta_frequente_alter_anexo_arquivo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivo',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='percentual_similaridade_resposta',
            field=slth.db.models.IntegerField(null=True, verbose_name='Percentual de Simiralidade da Resposta'),
        ),
        migrations.CreateModel(
            name='ArquivoCliente',
            fields=[
                ('arquivo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.arquivo')),
                ('cliente', slth.db.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Arquivo de Cliente',
                'verbose_name_plural': 'Arquivos de Cliente',
            },
            bases=('app.arquivo', slth.ModelMixin),
        ),
    ]