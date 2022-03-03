# Generated by Django 3.2.5 on 2022-03-03 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mbtiApp', '0001_initial'),
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('hobby_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('info', models.TextField(null=True)),
                ('user_id', models.ForeignKey(db_column='user_id', default='admin', on_delete=django.db.models.deletion.CASCADE, to='userApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='HobbyComment',
            fields=[
                ('h_cno', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('mbti_id', models.ForeignKey(db_column='mbti_id', on_delete=django.db.models.deletion.CASCADE, to='mbtiApp.mbti')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='userApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='HobbyLiked',
            fields=[
                ('hobby_id', models.ForeignKey(db_column='hobby_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hobbyApp.hobby')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='userApp.user')),
            ],
        ),
    ]