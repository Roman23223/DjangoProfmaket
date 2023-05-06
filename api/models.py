from django.db import models


class Work(models.Model):
    title = models.CharField("Наименование", max_length=255)
    content = models.TextField("Описание", max_length=1000)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField("Публиковать", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class Image(models.Model):
    title = models.CharField("Наименование", max_length=255)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Работа')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Address(models.Model):
    address = models.CharField('Адрес компании', max_length=255)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Адрес компании'
        verbose_name_plural = 'Адреса компании'


class Telephone_number(models.Model):
    number = models.CharField('Номер для связи', max_length=12)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Номер для связи'
        verbose_name_plural = 'Номера для связи'


class Email(models.Model):
    email = models.CharField('E-mail адрес', max_length=255)
    title = models.CharField('Наименование', max_length=255)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Электронная почта'
        verbose_name_plural = 'Электронные почты'


class Application(models.Model):
    size = models.CharField('Размер макета', max_length=255)
    product_time = models.CharField('Время изготовления', max_length=255)
    sender_name = models.CharField('Имя отправителя', max_length=20)
    number = models.CharField('Номер телефона', max_length=12)
    email = models.EmailField('Электронная почта', max_length=255)
    comment = models.TextField('Коментарий', max_length=1000)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
