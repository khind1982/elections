# Generated by Django 5.1.2 on 2024-10-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GEResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constituency', models.CharField(max_length=255)),
                ('conservative', models.IntegerField()),
                ('labour', models.IntegerField()),
                ('liberaldemocrat', models.IntegerField()),
                ('reform', models.IntegerField()),
                ('majority', models.IntegerField()),
            ],
        ),
    ]
