# Generated by Django 4.1.3 on 2023-03-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_rep_exe'),
    ]

    operations = [
        migrations.DeleteModel(
            name='rep_exe',
        ),
        migrations.AddField(
            model_name='person',
            name='idd',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]