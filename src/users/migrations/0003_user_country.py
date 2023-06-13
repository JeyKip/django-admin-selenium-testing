# Generated by Django 4.2 on 2023-06-13 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('users', '0002_alter_user_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='locations.country', verbose_name='Country'),
        ),
    ]