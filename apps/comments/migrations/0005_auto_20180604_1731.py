# Generated by Django 2.0.5 on 2018-06-04 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20180527_1327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'get_latest_by': 'submit_time', 'ordering': ['submit_time'], 'verbose_name': '回复', 'verbose_name_plural': '回复'},
        ),
    ]
