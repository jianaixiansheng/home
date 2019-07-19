# Generated by Django 2.1.3 on 2019-07-18 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0002_auto_20190715_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_reply', models.CharField(max_length=300)),
                ('comment_fk_house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='body.house')),
                ('comment_fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='body.UserInfo')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_connent',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_reply',
            field=models.TextField(blank=True),
        ),
    ]