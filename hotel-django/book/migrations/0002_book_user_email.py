# Generated by Django 3.0 on 2019-12-16 07:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='user_email',
            field=models.EmailField(default=datetime.datetime(2019, 12, 16, 7, 59, 9, 198959, tzinfo=utc), max_length=254, verbose_name='Correo electrónico del usuario'),
            preserve_default=False,
        ),
    ]
