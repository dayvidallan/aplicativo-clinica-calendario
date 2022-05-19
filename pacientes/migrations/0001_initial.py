# Generated by Django 3.2.13 on 2022-05-18 16:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True, verbose_name='Nº CPF')),
                ('rg', models.CharField(blank=True, max_length=14, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=14, null=True, verbose_name='Sexo')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=100, verbose_name='Nº telefone celular')),
                ('endereco', models.CharField(max_length=100)),
                ('data_consulta', models.DateTimeField(default=django.utils.timezone.now)),
                ('anamnesi', models.TextField(blank=True, null=True, verbose_name='Ananimese')),
                ('upload', models.FileField(blank=True, null=True, upload_to='perfil')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_consulta', models.DateTimeField(default=django.utils.timezone.now)),
                ('anamnesi', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ananimese')),
                ('upload', models.FileField(blank=True, null=True, upload_to='upload', verbose_name='Documentos')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]