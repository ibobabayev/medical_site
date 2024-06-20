from django.db import models
from django.conf import settings

Nullable = {'null': True, 'blank': True}


class Hospitals(models.Model):
    name = models.CharField(max_length=200, verbose_name='название клиники')
    description = models.TextField(verbose_name='описание клиники')
    location = models.TextField(verbose_name='адрес клиники')
    preview = models.ImageField(upload_to='hospitals/', verbose_name='фотография клиники', **Nullable)
    email = models.EmailField(unique=True, verbose_name='email')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='владелец',default=1)


    def __str__(self):
        return f"Клиника {self.name} в {self.location}"

    class Meta:
        verbose_name = 'Клиника'
        verbose_name_plural = 'Клиники'


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='отделения медицины')
    description = models.TextField(verbose_name='описание департамента')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='владелец',default=1)


    def __str__(self):
        return f"Отделения {self.name}"

    class Meta:
        verbose_name = 'Отделения'
        verbose_name_plural = 'Отделении'


class Doctors(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='имя врача')
    last_name = models.CharField(max_length=50, verbose_name='фамилия врача')
    avatar = models.ImageField(upload_to='doctors/', verbose_name='фотография врача', **Nullable)
    year_of_experience = models.IntegerField(verbose_name='опыт работы')
    department = models.ForeignKey(Department, verbose_name='отделение', on_delete=models.SET_NULL,**Nullable)
    hospital = models.ForeignKey(Hospitals, verbose_name='клиника', on_delete=models.SET_NULL, **Nullable)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='владелец',default=1)


    def __str__(self):
        return f"Врач {self.first_name} {self.last_name} работает в отделении {self.department} в клинике {self.hospital}"

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(upload_to='product/', verbose_name='изображение', **Nullable)
    price = models.IntegerField(verbose_name='цена')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='владелец',default=1)


    def __str__(self):
        return f'Имя продукта: {self.name}  Цена: {self.price} рублей'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Blog(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя")
    slug = models.CharField(max_length=50, verbose_name="slug")
    description = models.TextField(verbose_name='содержание')
    preview = models.ImageField(upload_to='blog/', verbose_name='изображение', **Nullable)
    created_at = models.DateField(verbose_name='дата создания', auto_now_add=True, **Nullable)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name='владелец',
                              on_delete=models.SET_NULL)
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f"{self.name}, {self.description}, {self.created_at}"

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    number = models.TextField(verbose_name='номер телефона')
    email = models.EmailField(verbose_name='email')

    def __str__(self):
        return f'{self.name} {self.number}'

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
