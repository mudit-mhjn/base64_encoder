# Generated by Django 2.2.3 on 2020-06-15 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_tag', models.TextField(max_length=20)),
                ('image_main', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
