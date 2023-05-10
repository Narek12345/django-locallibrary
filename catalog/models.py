from django.db import models
from django.urls import reverse

import uuid


class Genre(models.Model):
	"""Модель, представляющая книжный жанр (например, научная фантастика, документальная литература)."""
	name = models.CharField(max_length=200, help_text="Введите жанр книги (например, научная фантастика, французская поэзия)")


	def __str__(self):
		"""Строка для представления обьекта модели."""
		return self.name



class Book(models.Model):
	"""Модель, представляющая книгу."""
	title = models.CharField(max_length=200)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000, help_text="Введите краткое описание книги")
	isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genre = models.ManyToManyField(Genre, help_text="Выберите жанр для этой книги")


	def __str__(self):
		"""Строка для представления обьекта модели."""
		return self.title


	def get_absolute_url(self):
		"""Возвращает URL адрес для доступа к конкретному экземпляру книги."""
		return reverse('book-detail', args=[str(self.id)])


	def display_genre(self):
		"""Создаем строку для Genre. Это необходимо для отображения жанра в Admin."""
		print(type(self))
		return ', '.join([ genre.name for genre in self.genre.all()[:3]])

	display_genre.short_description = 'Genre'



class BookInstance(models.Model):
	"""Модель, представляющая конкретный экземпляр книги (т.е. который можно взять в библиотеке)."""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Уникальный идентификатор этой конкретной книги во всей библиотеке")
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
		('o', 'Maintenance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	)

	status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text="Забронировать наличие мест")

	
	class Meta:
		ordering = ['due_back']


	def __str__(self):
		"""Строка для представления обьекта модели."""
		return f'{self.book} {self.id}'



class Author(models.Model):
	"""Модель, представляющая автора."""
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)


	def get_absolute_url(self):
		"""Возвращает URL адрес доступа к конкретному экземпляру автора."""
		return reverse('author-detail', args=[str(self.id)])


	def __str__(self):
		"""Строка для представления обьекта модели."""
		return f"{self.last_name} {self.first_name}"