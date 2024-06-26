# Generated by Django 5.0.6 on 2024-06-14 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('slug', models.CharField(max_length=50, verbose_name='slug')),
                ('description', models.TextField(verbose_name='содержание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='изображение')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='дата создания')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('number', models.TextField(verbose_name='номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='отделения медицины')),
                ('description', models.TextField(verbose_name='описание департамента')),
            ],
            options={
                'verbose_name': 'Отделения',
                'verbose_name_plural': 'Отделении',
            },
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='имя врача')),
                ('last_name', models.CharField(max_length=50, verbose_name='фамилия врача')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='doctors/', verbose_name='фотография врача')),
                ('year_of_experience', models.IntegerField(verbose_name='опыт работы')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
            },
        ),
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название клиники')),
                ('description', models.TextField(verbose_name='описание клиники')),
                ('location', models.TextField(verbose_name='адрес клиники')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='hospitals/', verbose_name='фотография клиники')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
            ],
            options={
                'verbose_name': 'Клиника',
                'verbose_name_plural': 'Клиники',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.TextField(verbose_name='описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='изображение')),
                ('price', models.IntegerField(verbose_name='цена')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
