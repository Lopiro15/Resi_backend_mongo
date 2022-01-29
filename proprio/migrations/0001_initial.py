# Generated by Django 4.0.1 on 2022-01-29 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historiqueresi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('idresidence', models.CharField(max_length=255)),
                ('idclient', models.CharField(max_length=255)),
                ('tempssurannonce', models.IntegerField()),
                ('visite3D', models.BooleanField(default=False)),
                ('residencecommandé', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imageresi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idresidence', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='proprio/image/resi/')),
            ],
        ),
        migrations.CreateModel(
            name='Proprietaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('prenoms', models.CharField(max_length=75)),
                ('phone', models.CharField(max_length=10)),
                ('photo', models.ImageField(null=True, upload_to='proprio/image/')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idproprio', models.CharField(max_length=255)),
                ('descriptifresidence', models.TextField()),
                ('ville', models.CharField(max_length=100)),
                ('quartier', models.CharField(max_length=100)),
                ('prix', models.IntegerField()),
                ('disponibilité', models.BooleanField(default=True)),
                ('photocouverture', models.ImageField(null=True, upload_to='proprio/image/resi/')),
            ],
        ),
    ]