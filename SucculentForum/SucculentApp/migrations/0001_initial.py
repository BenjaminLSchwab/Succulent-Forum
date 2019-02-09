# Generated by Django 2.1.5 on 2019-02-02 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('DateUpdated', models.DateField()),
                ('Body', models.CharField(max_length=50)),
                ('ViewCount', models.IntegerField()),
                ('DateStarted', models.DateField()),
                ('PostCount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('DateUpdated', models.DateField()),
                ('ThreadCount', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='thread',
            name='TopicId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SucculentApp.Topic'),
        ),
        migrations.AddField(
            model_name='thread',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]