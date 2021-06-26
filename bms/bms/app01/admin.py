from django.contrib import admin
from .models import Author, Book, Publisher
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    pass

class PublisherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author,AuthorAdmin),
admin.site.register(Book, BookAdmin),
admin.site.register(Publisher, PublisherAdmin)
