# Generated by Django 4.0.4 on 2022-11-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0002_contact_alter_garbage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user_product',
            field=models.ManyToManyField(blank=True, to='hackathon.userprofile'),
        ),
    ]