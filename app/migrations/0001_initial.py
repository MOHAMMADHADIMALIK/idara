# Generated by Django 5.0 on 2024-05-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dropdownoptions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cord', models.CharField(max_length=50, null=True)),
                ('accounttype', models.CharField(max_length=50, null=True)),
                ('ledgerhead', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]