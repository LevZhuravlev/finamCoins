from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


import random
import string

from django.utils.text import slugify
import transliterate


def gen_slug(name, secondName):
    new_slug_part_one = slugify(name, allow_unicode=True)
    new_slug_part_two = slugify(secondName, allow_unicode=True)

    try:
        new_slug_part_one = transliterate.translit(new_slug_part_one, reversed=True)
        new_slug_part_two = transliterate.translit(new_slug_part_two, reversed=True)

    except:
        try:
            new_slug_part_two = transliterate.translit(new_slug_part_two, reversed=True)
        except:
            try:
                new_slug_part_two = transliterate.translit(new_slug_part_two, reversed=True)
            except:
                pass
    new_slug_part_one = new_slug_part_one.replace("\'", "")
    new_slug_part_two = new_slug_part_two.replace("\'", "")

    return new_slug_part_one + new_slug_part_two


def gen_nick(name, secondName):
    new_slug_part_one = slugify(name, allow_unicode=True)
    new_slug_part_two = slugify(secondName, allow_unicode=True)

    try:
        new_slug_part_one = transliterate.translit(new_slug_part_one, reversed=True)
        new_slug_part_two = transliterate.translit(new_slug_part_two, reversed=True)

    except:
        try:
            new_slug_part_one = transliterate.translit(new_slug_part_one, reversed=True)
        except:
            try:
                new_slug_part_two = transliterate.translit(new_slug_part_two, reversed=True)
            except:
                pass
    new_slug_part_one = new_slug_part_one.replace("\'", "")
    new_slug_part_two = new_slug_part_two.replace("\'", "")

    userNick = new_slug_part_one + new_slug_part_two

    def checkingUserName(name):
        try:
            User.objects.get(name=name)
            name += name[random.randint(0, len(name))]
            checkingUserName(name)
        except:
            return name

    return checkingUserName(userNick)



# Create your models here.

import datetime
from django.utils import timezone


# Модель акций
class Equities(models.Model):
    company_name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=150, null=True, blank=True, unique=True)
    price = models.IntegerField()
    company_label = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name="company_logo")
    company_label_url = models.URLField(null=True, blank=True)
    company_url = models.URLField(null=True, blank=True, default='https://www.finam.ru')
    date_of_last_update = models.DateField(default=timezone.now)

    def __str__(self):
        return self.company_name


# Модель групп
class Groups(models.Model):
    group_name = models.CharField("Имя группы",
                                  max_length=30,
                                  unique=True)
    slug = models.SlugField(max_length=150, null=True, blank=True, unique=True)

    LITTLE = 'Little'
    MIDDLE = 'Middle'
    OLD = 'Old'

    AGE_CHOICES = [
        (LITTLE, '7-10 лет'),
        (MIDDLE, '10-14 лет'),
        (OLD, '14-17 лет'),
    ]

    group_age = models.CharField("Возраст",
                                 blank=True,
                                 null=True,
                                 max_length=7,
                                 choices=AGE_CHOICES,
                                 default=MIDDLE)

    slug = models.SlugField(max_length=150, null=True, blank=True, unique=True)

    def __str__(self):
        return self.group_name

    def save(self, *args, **kwargs):
        if not self.id:
            slug = gen_slug(self.group_name, self.group_age)
            self.slug = slug

        super().save(*args, **kwargs)

from django.core.validators import MaxValueValidator, MinValueValidator


# Модель Ученика
class StudentsInfo(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=150, null=True, blank=True, unique=True)

    name = models.CharField("Имя", blank=False, null=True, max_length=32)
    second_name = models.CharField("Фамилия", blank=False, null=True, max_length=32)
    father_name = models.CharField("Отчество", blank=True, null=True, max_length=32)
    date_of_birth = models.DateField("Дата рождения", blank=True, null=True)
    phone_number = models.CharField("Номер телефона", blank=True, null=True, max_length=32)

    password = models.CharField("Password", blank=True, null=True, max_length=32)

    coins = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    notifications = models.TextField("Уведомеления", blank=False, null=True, max_length=4000)

    # Status
    STUDENT = 'ST'
    DELETED_USER = 'DU'
    GRADUATE = 'GR'

    STATUS_CHOICES = [(STUDENT, 'Ученик'), (DELETED_USER, 'Удаленный студент'), (GRADUATE, 'Выпускник')]

    status_name = models.CharField(blank=True, null=True, max_length=2, choices=STATUS_CHOICES, default=STUDENT, )
    group = models.ForeignKey(Groups, on_delete=models.SET_NULL, blank=True, null=True)
    equities = models.ManyToManyField(Equities, blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.id:
            slug = gen_slug(self.name, self.second_name)
            self.slug = slug

            name = gen_nick(self.name, self.second_name)
            pas = ''
            for i in range(random.randint(8, 16)):
                pas = pas + str(name[random.randint(0, len(name) - 1)])
            self.user_name = User.objects.create_user(username=self.slug, password=pas)
            self.password = pas

        super().save(*args, **kwargs)


from .tests import sendMail

# Модель преподавателя
class TeachersInfo(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    who_add_me = models.ForeignKey(User, related_name='who_add_me', on_delete=models.SET_NULL, null=True,)
    is_super_user = models.BooleanField("Суперадмин", default=False)
    slug = models.SlugField(max_length=150, null=True, blank=True, unique=True)
    email = models.EmailField("Адрес электронной почты", max_length=32, unique=True)
    name = models.CharField("Имя", blank=False, null=True, max_length=32)
    second_name = models.CharField("Фамилия", blank=False, null=True, max_length=32)
    phone_number = models.CharField("Номер телефона", blank=True, null=True, max_length=32)

    password = models.CharField("Пароль", blank=True, null=True, max_length=32, )

    group = models.ManyToManyField(Groups, blank=True)

    def __str__(self):
        return str(self.user_name)

    def save(self, *args, **kwargs):
        if not self.id:
            slug = gen_slug(self.name, self.second_name)
            self.slug = slug

            name = gen_nick(self.name, self.second_name)
            name.replace("\'", "")
            pas = ''
            for i in range(random.randint(8, 16)):
                pas = pas + str(name[random.randint(0, len(name) - 1)])
            try:
                if self.is_super_user:
                    self.user_name = User.objects.create_superuser(username=self.slug, password=pas)
                else:
                    self.user_name = User.objects.create_user(username=self.slug, password=pas)
            except:
                self.user_name = User.objects.create_user(username=self.slug, password=pas)

            self.password = pas

            message = 'Вы успешно зарегестрированны на FimCoin\n Логин для входа: ' + str(self.user_name) + '\n Пароль: ' +  str(self.password)
            sendMail(self.email, message)
        super().save(*args, **kwargs)
