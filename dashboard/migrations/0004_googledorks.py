# Generated by Django 4.0.3 on 2022-04-03 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_githubdorks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Googledorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dork_name', models.CharField(default='Dork Name', max_length=30)),
                ('dork_category', models.IntegerField(default=0)),
            ],
        ),
    ]
