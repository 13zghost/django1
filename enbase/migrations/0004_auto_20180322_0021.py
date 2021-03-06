# Generated by Django 2.0.3 on 2018-03-21 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enbase', '0003_auto_20180322_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('global_id', models.IntegerField(primary_key=True, serialize=False)),
                ('local_id', models.IntegerField()),
                ('name', models.CharField(max_length=300)),
                ('quality', models.FloatField()),
                ('scenario', models.BooleanField()),
                ('date', models.CharField(max_length=20)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enbase.GameDomain')),
            ],
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='games',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enbase.GameType'),
        ),
    ]
