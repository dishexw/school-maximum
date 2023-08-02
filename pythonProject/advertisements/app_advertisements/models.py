from django.db import models

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
        return f"id={self.id}, first_name={self.first_name}, price={self.price}"