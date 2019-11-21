# Generated by Django 2.1.1 on 2019-11-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]