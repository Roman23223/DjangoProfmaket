from django.db import models
from django.template import loader
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


class Work(models.Model):
    title = models.CharField("Наименование", max_length=255)
    content = models.TextField("Описание", max_length=1000)
    time_create = models.DateTimeField("Дата создания", auto_now_add=True, null=True, blank=True)
    time_update = models.DateTimeField("Дата обновления", auto_now=True, null=True, blank=True)
    is_published = models.BooleanField("Публиковать", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class Image(models.Model):
    title = models.CharField("Наименование", max_length=255)
    image = models.ImageField("Ссылка на изображение", upload_to='images', null=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Работа', related_name='images')

    def short_description(self):
        return truncatechars(self.description, 20)

    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')
    img_preview.short_description = 'Изображение'

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
    number = models.CharField('Номер для связи', max_length=16, help_text='В формате +7(000)000-00-00')

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
    sender_name = models.CharField('Имя заказчика', max_length=20)
    number = models.CharField('Номер телефона', max_length=16)
    email = models.EmailField('Электронная почта', max_length=255)
    comment = models.TextField('Коментарий', max_length=1000, null=True, blank=True)
    time_create = models.DateTimeField("Отправлено", auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


@receiver(post_save, sender=Application)
def send(sender, instance, **kwargs):
    if kwargs['created']:
        html_messsage = loader.render_to_string(
            'email_messages/html_message.html',
            {
                'sender_name': instance.sender_name,
                'number': instance.number,
                'email': instance.email,
                'size': instance.size,
                'product_time': instance.product_time,
                'comment': instance.comment,
            }
        )

        send_mail(
            "Заказ",
            None,
            settings.EMAIL_HOST_USER,
            ['roma_chepiga@mail.ru'],
            fail_silently=False,
            html_message=html_messsage
        )
