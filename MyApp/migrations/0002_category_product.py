# Generated by Django 4.2.4 on 2023-09-02 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('createBy', models.IntegerField()),
                ('updateBy', models.IntegerField()),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('barcode', models.BigIntegerField()),
                ('unitPrice', models.FloatField()),
                ('qtyInstock', models.IntegerField()),
                ('photo', models.ImageField(upload_to='media/')),
                ('createBy', models.IntegerField()),
                ('updateBy', models.IntegerField()),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('updateAt', models.DateTimeField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.category')),
            ],
        ),
    ]
