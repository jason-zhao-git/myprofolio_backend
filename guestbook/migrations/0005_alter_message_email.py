# Generated by Django 5.0.6 on 2024-06-30 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0004_rename_guestbookmessage_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]