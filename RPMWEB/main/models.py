from django.db import models

class Person(models.Model):

    first_name = models.CharField("Имя", max_length=30)

    last_name = models.CharField("Фамилия", max_length=30)

    group = models.CharField("Группа", max_length=6)

    email = models.EmailField("Адресс электронной почты", max_length=254)

    test_level = models.IntegerField("Уровень способностей")

class Work(models.Model):

    work_description = models.TextField("Описание работы", max_length=250)

    required_level = models.IntegerField("Требуемый уровень")

    reward = models.CharField("Награда", max_length=30)

class Test(models.Model):

    test_description = models.TextField("Описание теста", max_length=250)

    required_level = models.IntegerField("Требуемый уровень")

    resulting_level = models.IntegerField("Получаемый уровень")
