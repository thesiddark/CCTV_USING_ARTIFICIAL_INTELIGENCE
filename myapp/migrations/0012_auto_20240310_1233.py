# Generated by Django 2.2.24 on 2024-03-10 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_detection_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detection',
            name='did',
        ),
        migrations.AddField(
            model_name='detection',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.User'),
            preserve_default=False,
        ),
    ]
