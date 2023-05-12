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

	# Количество посещений этого представления, подсчитанное в переменной сеанса.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1


	context={'num_books': num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_available, 'num_authors': num_authors, 'num_visits': num_visits}

	return render(request, 'index.html', context)


class BookListView(generic.ListView):
	model = Book
	paginate_by = 10


class BookDetailView(generic.DetailView):
	model = Book


class AuthorListView(generic.ListView):
	model = Author
	paginate_by = 10


class AuthorDetailView(generic.DetailView):
	model = Author