# Generated by Django 2.2 on 2019-04-26 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190426_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
