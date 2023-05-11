from django.views import generic
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre


def index(request):
	"""Функция отображения для домашней страницы сайта."""
	
	# Генерация "количеств" некоторых главных обьектов.
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()

	# Доступные книги (статус = "а")
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.count()


	context={'num_books': num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_available, 'num_authors': num_authors}

	return render(request, 'index.html', context)


class BookListView(generic.ListView):
	model = Book
	paginate_by = 10


class BookDetailView(generic.DetailView):
	model = Book