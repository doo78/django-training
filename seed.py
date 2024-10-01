from django.core.management.base import BaseCommand
from faker import Faker
from loans.models import Book
import random

fake = Faker()

for _ in range(100):  # Generate 20 books
    book = Book(
        title=fake.sentence(nb_words=3),
        authors=fake.name(),
        publication_date=fake.date_between(start_date='-30y', end_date='today'),
        isbn=fake.isbn13()
    )
    book.save()

