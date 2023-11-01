# Generated by Django 4.1.7 on 2023-04-20 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enotes', '0007_notes_is_important_delete_reminder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='noteTitle',
        ),
        migrations.AddField(
            model_name='notes',
            name='tags',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
