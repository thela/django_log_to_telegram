# Generated by Django 2.1.5 on 2020-01-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_log_to_telegram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botdata',
            name='bot_token',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='botdata',
            name='chat_id',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]