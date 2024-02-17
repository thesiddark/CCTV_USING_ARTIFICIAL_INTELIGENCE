# Generated by Django 5.0.1 on 2024-02-13 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_detect_criminal_detect_image_detect_sub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detect_sub',
            name='DETECT',
        ),
        migrations.RemoveField(
            model_name='detect_sub',
            name='CRIMINAL',
        ),
        migrations.CreateModel(
            name='detection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=100)),
                ('CRIMINAL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.criminals')),
            ],
        ),
        migrations.DeleteModel(
            name='detect',
        ),
        migrations.DeleteModel(
            name='detect_sub',
        ),
    ]