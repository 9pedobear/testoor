from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


User = get_user_model()


class Employer(models.Model):                # Создаем таблицу с названием
    # Сотрудников
    name = models.CharField(                 # Поле ФИО сотрудников
        verbose_name='ФИО',                  # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True)                           # Аргумент для обозначения поля
        # пустым
    city = models.ForeignKey(                # Поле для выбора города
        'Location',                          # Аргумент связи с таблицей
        # содержащий список городов
        verbose_name='Город',                # Аргумент для альтернативного
        # имени поля
        on_delete=models.CASCADE,            # Аргумент для определения как
        # удалять информацию в случае удаления поля
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True)                           # Аргумент для обозначения поля
        # пустым
    work = models.ManyToManyField(           # Поле для выбора Деятельности
        'Activity',                          # Аргумент связи с таблицей
        verbose_name='Деятельность',         # Аргумент для альтернативного
        # имени поля
        related_name='activity',             # указывает имя обратной связи
        # из модели Activity обратно в вашу модель.
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
    )
    direction = models.ManyToManyField(      # Поле для выбора Направлений
        'Category',                          # Аргумент связи с таблицей
        verbose_name='Направление',          # Аргумент для альтернативного
        # имени поля
        related_name='category',             # указывает имя обратной связи
        # из модели Category обратно в вашу модель.
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
    )
    description = models.TextField(          # Поле для ввода Описания
        verbose_name='Описание',             # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True)                           # Аргумент для обозначения поля
        # пустым
    education = models.ManyToManyField(      # Поле для выбора Образования
        'Education',                         # Аргумент связи с таблицей
        verbose_name='Образование',          # Аргумент для альтернативного
        # имени поля
        related_name='education',            # указывает имя обратной связи
        # из модели Education обратно в вашу модель.
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
    )
    experience = models.CharField(           # Поле для Стажа
        verbose_name='Стаж',                 # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True                            # Аргумент для обозначения поля
        # пустым
    )
    cabinet = models.ManyToManyField(        # Поле для выбора Кабинета
        'Adress',                            # Аргумент связи с таблицей
        verbose_name='Кабинет',              # Аргумент для альтернативного
        # имени поля
        related_name='adress',               # указывает имя обратной связи
        # из модели Adress обратно в вашу модель.
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
    )
    personal_consultation = models.CharField(# Поле для назначения Личной
        # встречи
        verbose_name='Личная встреча',       # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True                            # Аргумент для обозначения поля
        # пустым
    )
    online_consultation = models.CharField(  # Поле для Онлайн-консультация
        verbose_name='Онлайн-консультация',  # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True                            # Аргумент для обозначения поля
        # пустым
    )
    duration_consultation = models.CharField(# Поле для Длительность консультации
        verbose_name='Длительность консультации', # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True                            # Аргумент для обозначения поля
        # пустым
    )
    couple_consultation_duration = models.CharField(# Поле для Длительность консультации для пар
        verbose_name='Длительность консультации для пар', # Аргумент для альтернативного
        # имени поля
        max_length=1000,                     # Аргумент для максимального
        # количества знаков (обязательный)
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True                            # Аргумент для обозначения поля
        # пустым
    )
    photo = models.ImageField(               # Поле для Фото
        verbose_name='Фото',                 # Аргумент для альтернативного
        # имени поля
        upload_to='photos/%Y/%m/%d/',        # Аргумент для указания пути
        # сохранения фото
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
        null=True                            # Аргумент для обозначения поля
        # пустым
    )
    created = models.DateTimeField(          # Поле для даты
        verbose_name='Дата публикации',      # Аргумент для альтернативного
        # имени поля
        auto_now_add=True,                   # Аргумент автодобавления даты
        blank=True,                          # Аргумент для обозначения поля
        # не обязательным для заполнения
    )
    updated = models.DateTimeField(          # Поле для выбора города
        verbose_name='Обновлено',            # Аргумент для альтернативного
        # имени поля
        auto_now=True,                       # Аргумент автодобавления даты
        blank=True                           # Аргумент для обозначения поля
        # не обязательным для заполнения
    )
    is_published = models.BooleanField(      # Поле для определения
        # опубликованно или нет
        verbose_name='Опубликовано',         # Аргумент для альтернативного
        # имени поля
        default=True,                        # Аргумент для вставки
        # состояния "Опубликовано" по умолчанию
        blank=True                           # Аргумент для обозначения поля
        # не обязательным для заполнения
    )

    def get_absolute_url(self):              # Метод для получения ссылки на
        # таблицу
        return reverse(                      # Возвращаем ссылку на таблицу
            'view_employer',                 # Имя возрвращаемой таблицы
            kwargs={"pk": self.pk}           # Берем из поля id ссылку на
            # таблицу
        )

    def __str__(self):                       # Вывод данных в строковом виде
        return f'''{self.name} -  
        "{self.description}"
        {self.direction} -
        {self.education} -
        {self.experience} лет
        {self.cabinet} -
        {self.personal_consultation} -
        {self.online_consultation} -
        {self.duration_consultation} минут
        {self.couple_consultation_duration} минут
        '''                                  # Обозначаем поля

    class Meta:                              # Расширяем возможность класса
        verbose_name = 'Специалист'          # Имя таблицы в единственном числе
        verbose_name_plural = 'Специалисты'  # Имя таблицы во множественном
        # числе
        ordering = ['name']                  # Сортировка полю имени


class Adress(models.Model):
    cabinet = models.CharField(
        verbose_name='Кабинет',
        max_length=1000,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse('view_adress', kwargs={"pk": self.pk})

    def __str__(self):
        return f'''{self.cabinet} -
        '''

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ['cabinet']


class Education(models.Model):
    university = models.CharField(
        verbose_name='Университет',
        max_length=1000,
        blank=True,
        null=True
    )
    skill = models.CharField(
        verbose_name='Квалификация',
        max_length=1000,
        blank=True,
        null=True
    )
    education_date = models.DateTimeField(
        verbose_name='Год получения',
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse('view_education', kwargs={"pk": self.pk})

    def __str__(self):
        return f'''{self.university} -
        {self.skill} -
        {self.education_date} -
        '''

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'
        ordering = ['university']


class Category(models.Model):
    direction = models.CharField(
        'Направление',
        max_length=1000,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse('view_category', kwargs={"pk": self.pk})

    def __str__(self):
        return f'''- {self.direction}
        '''

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['direction']


class Activity(models.Model):
    work = models.CharField(
        'Деятельность',
        max_length=1000,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse('view_activity', kwargs={"pk": self.pk})

    def __str__(self):
        return f'''- {self.work}
        '''

    class Meta:
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельность'
        ordering = ['work']


class Location(models.Model):
    city = models.CharField(
        'Город',
        max_length=1000,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse('view_location', kwargs={"pk": self.pk})

    def __str__(self):
        return f'''г. {self.city} 
        '''

    class Meta:
        verbose_name = 'Местонахождение'
        verbose_name_plural = 'Местонахождения'
        ordering = ['city']
