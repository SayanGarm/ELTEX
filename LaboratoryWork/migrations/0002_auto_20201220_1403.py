# Generated by Django 3.1.2 on 2020-12-20 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LaboratoryWork', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboratoryWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('document', models.FileField(upload_to='', verbose_name='Документ')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='laboratory_work',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='LaboratoryWork.laboratorywork', verbose_name='Лабораторная работа'),
        ),
    ]