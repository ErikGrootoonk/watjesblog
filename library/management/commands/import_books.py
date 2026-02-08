import json

from django.core.management.base import BaseCommand

from library.models import Book


class Command(BaseCommand):
    help = "Import books from boekenlijst.json"

    def add_arguments(self, parser):
        parser.add_argument("file", help="Path to the JSON file")

    def handle(self, *args, **options):
        with open(options["file"], encoding="utf-8") as f:
            data = json.load(f)

        count = 0
        for entry in data:
            author = f"{entry['voornaam']} {entry['achternaam']}".strip()
            Book.objects.get_or_create(
                title=entry["titel"],
                author=author,
                defaults={
                    "description": entry.get("beschrijving", ""),
                    "language": entry.get("Taal", ""),
                },
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(f"Imported {count} books"))
