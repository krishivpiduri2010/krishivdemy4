# Generated by Django 3.2.6 on 2021-08-11 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('krishivdemy_app', '0008_auto_20210811_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='image', max_length=7, null=True)),
                ('order', models.IntegerField(null=True)),
                ('file_name', models.CharField(max_length=40)),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='krishivdemy_app.page')),
            ],
        ),
    ]
