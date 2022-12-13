# Generated by Django 4.1 on 2022-11-28 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteApp', '0005_image_todolist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='cover')),
                ('pdf', models.FileField(upload_to='pdf')),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]
