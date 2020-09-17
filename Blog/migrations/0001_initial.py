# Generated by Django 3.0.8 on 2020-07-06 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_header', models.CharField(max_length=30)),
                ('article_text', models.TextField(default='here comes text')),
                ('article_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Author')),
            ],
        ),
    ]
