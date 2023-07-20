# Generated by Django 4.2.3 on 2023-07-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('data', models.TextField()),
                ('voqt', models.DateTimeField()),
                ('values', models.TextField()),
            ],
        ),
    ]
