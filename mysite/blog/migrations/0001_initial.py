# Generated by Django 2.1.3 on 2018-12-14 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('body', models.TextField(blank=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
