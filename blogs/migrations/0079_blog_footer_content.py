# Generated by Django 4.0.4 on 2022-11-29 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0078_blog_analytics_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='footer_content',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
