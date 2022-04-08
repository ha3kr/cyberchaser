# Generated by Django 4.0.3 on 2022-03-30 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=30)),
                ('subdomains', models.TextField()),
                ('acquisitions', models.TextField()),
            ],
        ),
    ]
