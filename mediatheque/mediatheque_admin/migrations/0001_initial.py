# Generated by Django 5.0.7 on 2024-07-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emprunteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('bloque', models.BooleanField(default=False)),
            ],
        ),
    ]
