# Generated by Django 4.2.3 on 2023-09-02 12:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_delete_webscraper_alter_word_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="word",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]