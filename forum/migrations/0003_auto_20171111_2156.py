# Generated by Django 2.0b1 on 2017-11-11 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20170618_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='板块名称')),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间 ')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='plate',
        ),
        migrations.DeleteModel(
            name='Plate',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='forum.Category'),
        ),
    ]