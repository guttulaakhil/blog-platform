# Generated by Django 2.0.7 on 2018-08-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180811_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='blogs',
            field=models.ManyToManyField(blank=True, related_name='tags', to='blog.Blog'),
        ),
    ]