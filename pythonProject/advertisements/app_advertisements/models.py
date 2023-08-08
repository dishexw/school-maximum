from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
# Create your models here.


class Advertisement(models.Model):
    first_name = models.CharField("Заголовок", max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметье, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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


