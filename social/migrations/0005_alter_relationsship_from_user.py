# Generated by Django 3.2.5 on 2021-07-26 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0004_auto_20210726_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationsship',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationsships', to=settings.AUTH_USER_MODEL),
        ),
    ]
