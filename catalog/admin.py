from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


admin.site.register(Genre)



class BooksInline(admin.TabularInline):
	model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death'))
	inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
	model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('book', 'id', 'status', 'due_back', 'borrower')
	list_filter = ('status', 'due_back')

	fieldsets = (
		(None, {
			'fields': ('book', 'imprint', 'id')
		}),
		('Available', {
			'fields': ('status', 'due_back', 'borrower')
			}),
	)
