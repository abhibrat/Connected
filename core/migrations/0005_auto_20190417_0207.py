# Generated by Django 2.1.5 on 2019-04-16 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=5000)),
                ('commenter', models.TextField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.Post'),
        ),
    ]
