# Generated by Django 3.1.3 on 2020-12-16 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_auto_20201215_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='MY_USER_ID',
            field=models.CharField(blank=True, default='0', max_length=255, null=True),
        ),
    ]