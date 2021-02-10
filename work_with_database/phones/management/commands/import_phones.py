import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', newline='', encoding='utf-8') as csvfile:

            phone_reader = csv.DictReader(csvfile, delimiter=';')

            for line in phone_reader:
                slugg = slugify(line['name'], allow_unicode=True)
                phone = Phone(id=line['id'],name=line['name'],image=line['image'],price=line['price'],release_date=line['release_date'],lte_exists=line['lte_exists'],slug=slugg)
                phone.save()
