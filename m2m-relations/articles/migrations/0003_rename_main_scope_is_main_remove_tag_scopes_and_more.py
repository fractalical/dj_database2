# Generated by Django 4.1.7 on 2023-02-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope_tag_scope_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='main',
            new_name='is_main',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='scopes',
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='scopes', through='articles.Scope', to='articles.tag'),
        ),
    ]