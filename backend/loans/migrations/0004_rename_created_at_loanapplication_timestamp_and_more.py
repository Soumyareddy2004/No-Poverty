# Generated by Django 5.1.5 on 2025-02-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_alter_loanapplication_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanapplication',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
