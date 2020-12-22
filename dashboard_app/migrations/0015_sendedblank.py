# Generated by Django 3.1.3 on 2020-12-22 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard_app', '0014_auto_20201217_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendedBlank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('name_surname', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('amount', models.IntegerField()),
                ('credit_type', models.CharField(blank=True, max_length=100, null=True)),
                ('send_user_num', models.CharField(blank=True, default='0', max_length=255, null=True)),
                ('otp_status', models.BooleanField(default=False, verbose_name='otp status')),
                ('bank_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard_app.banklist')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]