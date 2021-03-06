# Generated by Django 2.2.6 on 2019-11-21 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191120_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(1, 'Komedia'), (2, 'S - F'), (0, 'Nieznany'), (4, 'Doramat'), (3, 'Horror')], default=0),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, default='', max_length=120)),
                ('starts', models.IntegerField(default=5)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Movie')),
            ],
        ),
    ]
