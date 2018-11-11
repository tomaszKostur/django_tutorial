# Generated by Django 2.1 on 2018-11-05 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_post_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='id',
        ),
        migrations.AlterField(
            model_name='autor',
            name='nickname',
            field=models.CharField(default='Guest', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forum.Autor'),
        ),
    ]
