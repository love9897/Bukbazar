# Generated by Django 3.2.5 on 2021-07-28 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('profile', models.ImageField(upload_to='authors/%Y/%m/%d')),
                ('signature', models.ImageField(upload_to='authors/signatures')),
                ('description', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('cover', models.ImageField(upload_to='books/')),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('pages', models.IntegerField()),
                ('chapters', models.IntegerField()),
                ('readers', models.IntegerField(default=0)),
                ('awards', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
    ]
