# Generated by Django 5.2.1 on 2025-05-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auta', '0017_alter_druh_popis_alter_druh_rok_zalozeni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='znacka',
            name='logo',
            field=models.ImageField(error_messages={'blank': 'Logo značky musí být vybráno'}, help_text='Vyberte logo značky', upload_to='znacky_loga/', verbose_name='Logo značky'),
        ),
    ]
