# Generated by Django 2.2.6 on 2019-11-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191120_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='info',
        ),
        migrations.AddField(
            model_name='movie',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(2, 'S - F'), (4, 'Doramat'), (0, 'Nieznany'), (3, 'Horror'), (1, 'Komedia')], default=0),
        ),
    ]
