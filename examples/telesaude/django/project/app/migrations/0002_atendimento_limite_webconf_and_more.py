# Generated by Django 4.2.6 on 2024-05-20 22:47

from django.db import migrations, models
import slth.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='limite_webconf',
            field=models.DateTimeField(null=True, verbose_name='Limite da WebConf'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='numero_webconf',
            field=slth.db.models.CharField(max_length=255, null=True, verbose_name='Número da WebConf'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='senha_webconf',
            field=slth.db.models.CharField(max_length=255, null=True, verbose_name='Senha da WebConf'),
        ),
    ]
