# Generated by Django 2.0 on 2019-06-27 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190627_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='descript',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]