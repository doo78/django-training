from django.core.management.base import BaseCommand
from loans.models import Book
import random

Book.objects.all().delete()