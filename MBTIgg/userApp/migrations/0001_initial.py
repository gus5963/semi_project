# Generated by Django 3.2.5 on 2022-03-03 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mbtiApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('birth', models.DateField()),
                ('pwd', models.CharField(max_length=60)),
                ('mbti_id', models.ForeignKey(db_column='mbti_id', on_delete=django.db.models.deletion.CASCADE, to='mbtiApp.mbti')),
            ],
        ),
    ]