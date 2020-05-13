import requests
from django.core.management.base import BaseCommand
from errata.models import Book


class Command(BaseCommand):
    help = "updates books from the CMS that are used on app"

    def handle(self, *args, **options):
        books_created = 0
        books_updated = 0

        r = requests.get('https://openstax.org/apps/cms/api/books')
        json = r.json()

        for cms_book in json['books']:
            book, created = Book.objects.get_or_create(cms_id=cms_book['id'])
            book.title = cms_book['title']
            book.save()

            if created:
                books_created = books_created + 1
            else:
                books_updated = books_updated + 1

        print('{} books created, {} books updated'.format(books_created, books_updated))
