# Generated by Django 2.0 on 2019-06-27 02:54

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190627_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=mdeditor.fields.MDTextField(null=True),
        ),
    ]
