# Generated by Django 3.2.5 on 2022-03-03 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mbti',
            fields=[
                ('mbti_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('defi', models.CharField(max_length=50)),
                ('profile', models.TextField()),
            ],
        ),
    ]