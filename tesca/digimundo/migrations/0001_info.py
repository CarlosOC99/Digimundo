# Generated by Django 3.2.9 on 2022-01-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90)),
                ('apellidos', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=30)),
                ('cargo', models.CharField(max_length=30)),
                ('comentarios', models.TextField()),
            ],
        ),
    ]
