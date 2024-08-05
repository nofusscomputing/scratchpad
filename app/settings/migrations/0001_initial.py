# Generated by Django 5.0.7 on 2024-07-12 03:55

import access.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

from django.contrib.auth.models import User

from settings.models.user_settings import UserSettings


def add_user_settings(apps, schema_editor):

    for user in User.objects.all():

        if not UserSettings.objects.filter(pk=user.id).exists():

            user_setting = UserSettings.objects.create(
                user=user
            )

            user_setting.save()



def add_app_settings(apps, schema_editor):

    app = apps.get_model('settings', 'appsettings')

    if not app.objects.filter(owner_organization=None).exists():

        setting = app.objects.create(
            owner_organization=None
        )

        setting.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('access', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created', access.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('modified', access.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('device_model_is_global', models.BooleanField(default=False, verbose_name='All Device Models are global')),
                ('device_type_is_global', models.BooleanField(default=False, verbose_name='All Device Types is global')),
                ('manufacturer_is_global', models.BooleanField(default=False, verbose_name='All Manufacturer / Publishers are global')),
                ('software_is_global', models.BooleanField(default=False, verbose_name='All Software is global')),
                ('software_categories_is_global', models.BooleanField(default=False, verbose_name='All Software Categories are global')),
                ('global_organization', models.ForeignKey(blank=True, default=None, help_text='Organization global items will be created in', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='global_organization', to='access.organization')),
                ('owner_organization', models.ForeignKey(blank=True, default=None, help_text='Organization the settings belong to', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_organization', to='access.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created', access.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('modified', access.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False)),
                ('default_organization', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='access.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(add_user_settings),
        migrations.RunPython(add_app_settings),
    ]
