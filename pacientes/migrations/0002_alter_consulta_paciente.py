# Generated by Django 3.2.13 on 2022-05-18 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to='pacientes.paciente'),
        ),
    ]
