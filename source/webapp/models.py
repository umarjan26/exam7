from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=300, null=False, blank=False, verbose_name='Название Опроса')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания опроса')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    text = models.TextField(max_length=3000,null=False, blank=False, verbose_name='Текст варианта' )
    poll = models.ForeignKey('webapp.Poll', related_name='choice', null=True, blank=False,
                                on_delete=models.CASCADE, verbose_name='Опрос')

