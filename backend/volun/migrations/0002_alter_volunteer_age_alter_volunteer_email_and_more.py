# Generated by Django 5.1.5 on 2025-02-08 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
