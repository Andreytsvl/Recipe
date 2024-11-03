from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, verbose_name="Логин")
    password = models.CharField(max_length=128, verbose_name="Пароль")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return self.username
