# Generated by Django 4.2.11 on 2024-04-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField()),
                ('username', models.CharField(max_length=255)),
                ('review_text', models.TextField()),
                ('published_data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
