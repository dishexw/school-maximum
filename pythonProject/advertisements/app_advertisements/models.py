from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

User = get_user_model()
# Create your models here.


class Advertisement(models.Model):
    first_name = models.CharField("Заголовок", max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметье, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/')

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f"Advertisement(id={self.id}, first_name={self.first_name}, price={self.price})"

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color: green; font-weight: bold">Сегодня в {}</span>', created_time
            )
        else:
            return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color: red; font-weight: bold">Сегодня в {}</span>', updated_time
            )
        else:
            return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Изображение')
    def image_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="50"/></a>'.format(self.image.url))
        else:
            return 'Нет изображения'
    image_img.short_description = 'Изображение'
    image_img.allow_tags = True


