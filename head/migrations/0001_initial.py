# Generated by Django 4.0.6 on 2022-11-21 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='especificoTDP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeImposto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('preco', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('ncm', models.FloatField()),
                ('situacaoTributaria', models.TextField(max_length=500)),
                ('categoriaEstado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='head.estado')),
                ('categoriaImposto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='head.tipodeimposto')),
                ('categoriaProdutos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='head.produtos')),
                ('categoriaServicos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='head.servicos')),
                ('categoriaespecificoTPD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='head.especificotdp')),
            ],
        ),
    ]
