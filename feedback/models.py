from django.db import models
from django.urls import reverse


class Feedback(models.Model):
    name = models.CharField(
        verbose_name='ФИО',
        max_length=1000,
        blank=True,
        null=True
    )
    question = models.CharField(
        verbose_name='Ваш вопрос',
        max_length=1000,
        blank=True,
        null=True
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=1000,
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse('view_feedback', kwargs={"pk": self.pk})

    def __str__(self):
        return f'''{self.name} -
        {self.question}
        {self.phone} -
        {self.created} -
        '''

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['name']