# Generated by Django 2.2.2 on 2019-07-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20190720_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logindetails',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='logindetails',
            name='mobile',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='logindetails',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]