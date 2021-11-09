# Generated by Django 3.2.6 on 2021-11-06 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mairie', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cooeperatives',
            options={'verbose_name_plural': 'Coopératives'},
        ),
        migrations.AlterModelOptions(
            name='members',
            options={'verbose_name_plural': 'Membres'},
        ),
        migrations.AddField(
            model_name='members',
            name='gender',
            field=models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], default='Femme', max_length=5),
        ),
        migrations.AlterField(
            model_name='members',
            name='cooeperative',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cooeperative', to='mairie.cooeperatives'),
        ),
        migrations.CreateModel(
            name='MemberComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Nom')),
                ('Subject', models.CharField(max_length=100, verbose_name='Sujet')),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField(verbose_name='Commentaire')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mairie.members')),
            ],
            options={
                'verbose_name': 'Commentaire',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='CooperativeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Nom')),
                ('Subject', models.CharField(max_length=100, verbose_name='Sujet')),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField(verbose_name='Commentaire')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('cooperatives', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mairie.cooeperatives')),
            ],
            options={
                'verbose_name': 'Commentaire',
                'ordering': ['-timestamp'],
            },
        ),
    ]