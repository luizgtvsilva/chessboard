# Generated by Django 3.2.9 on 2021-12-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChessB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece_name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('initial_position', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'chess',
            },
        ),
    ]
