# Generated by Django 4.0.3 on 2022-04-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_remove_program_subdomains_program_domains_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='myNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_name', models.CharField(default='Note Name', max_length=30)),
                ('note_content', models.TextField(default='Note description')),
            ],
        ),
    ]
