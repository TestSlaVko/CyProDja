# Generated by Django 4.0.4 on 2022-05-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0003_usercourses'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('subject', models.TextField()),
                ('note', models.TextField()),
            ],
        ),
    ]