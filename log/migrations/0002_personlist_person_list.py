# Generated by Django 4.1.3 on 2022-11-11 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='personList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='list',
            field=models.ForeignKey(default="none", on_delete=django.db.models.deletion.CASCADE, to='log.personlist'),
            preserve_default=False,
        ),
    ]
