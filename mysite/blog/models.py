from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

""" models.py – модели  данных  приложения.
 
class models — это объект определённого свойства: он хранится в базе данных. 
Это то место, где ты будешь хранить информацию о своих пользователях, записях в блоге и т.д. 
Мы будем использовать базу данных SQLite для хранения информации. 

любом  Django-приложении должен быть этот файл, но он может оставаться пустым; """

# Our custom manager.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


""" Обработчик (объект Manager) - это интерфейс, через который операции запросов к базе данных становятся доступными для моделей Django."""
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    """ такая таблица будет создана в Bd SQL  """
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')

    #objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    """ Meta внутренний класс в моделях Django: 
    Это просто контейнер класса с некоторыми параметрами (метаданными), прикрепленными к модели. 
    Он определяет такие вещи, как доступные разрешения, связанное имя таблицы базы данных, 
    является ли модель абстрактной или нет, единственной и множественной версиями имени и т.д """
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    """ get_absolute_url() связывает  модели с шаблонами и видами, и  формирует  URL-ссылки для выбранных записей из таблиц БД """
    def get_absolute_url(self):

        """ функция reverse -строит текущий URL-адрес записи на основе имени маршрута post и словаря параметров kwargs """
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
