# Generated by Django 4.0.4 on 2022-11-26 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0002_contact_alter_garbage_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(db_column='Category_ID', primary_key=True, serialize=False)),
                ('codename', models.CharField(db_column='Category_codename', max_length=250, unique=True)),
                ('name', models.CharField(blank=True, db_column='Category_name', max_length=250, null=True)),
                ('note', models.CharField(blank=True, db_column='Note', max_length=250, null=True)),
                ('create_date', models.DateField(auto_now_add=True, db_column='Created_date', null=True)),
                ('is_enable', models.BooleanField(blank=True, db_column='Enable', default=True, null=True)),
            ],
            options={
                'db_table': 'Category',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='user_product',
        ),
        migrations.AddField(
            model_name='product',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='edit_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='UserProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('cover_image', models.CharField(max_length=100)),
                ('video', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[('Trade', 'Trade'), ('Sell', 'Sell'), ('Borrow', 'Borrow'), ('Wanted', 'Wanted')], max_length=100, null=True)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('edit_date', models.DateTimeField(auto_now=True, null=True)),
                ('default_point', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hackathon.userprofile')),
            ],
            options={
                'db_table': 'UserProduct',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(max_length=100)),
                ('user_product_asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hackathon.userproduct')),
            ],
            options={
                'db_table': 'Asset',
                'managed': True,
            },
        ),
    ]
