# Generated by Django 2.1.2 on 2019-07-31 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0002_auto_20190715_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='pic_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='body.Photo'),
        ),
    ]