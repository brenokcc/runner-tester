# Generated by Django 4.2.6 on 2024-06-16 17:06

from django.db import migrations
import slth.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_atendimento_termo_assinado_especialista_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profissionalsaude',
            name='registro_profissional',
            field=slth.db.models.CharField(max_length=30, verbose_name='Registro Profissional'),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='bairro',
            field=slth.db.models.CharField(blank=True, max_length=40, null=True, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='cep',
            field=slth.db.models.CharField(blank=True, max_length=10, null=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='logradouro',
            field=slth.db.models.CharField(blank=True, max_length=120, null=True, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='numero',
            field=slth.db.models.CharField(blank=True, max_length=10, null=True, verbose_name='Número'),
        ),
    ]
