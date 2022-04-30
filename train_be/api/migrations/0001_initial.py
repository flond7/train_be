# Generated by Django 4.0.4 on 2022-04-29 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Railway',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=150)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('correct', models.BooleanField()),
                ('id_question', models.IntegerField()),
                ('id_user', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('surname', models.CharField(blank=True, default='', max_length=50)),
                ('mail', models.EmailField(max_length=150)),
                ('pw', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=150)),
                ('url', models.CharField(blank=True, default='', max_length=150)),
                ('duration', models.IntegerField()),
                ('railway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videoOfRailway', to='api.railway')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(default='')),
                ('answerOne', models.TextField(default='')),
                ('answerTwo', models.TextField(default='')),
                ('answerThree', models.TextField(default='')),
                ('correct', models.TextField(default='')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionOfVideo', to='api.video')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
