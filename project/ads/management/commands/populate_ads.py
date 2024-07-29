from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from ...models import Ad


class Command(BaseCommand):
    help = 'Populate ads data and create superuser'

    def handle(self, *args, **kwargs):
        ads = [
            {"title": "Ad 1", "ad_id": 1, "author": "Author 1", "views_count": 10, "position": 1},
            {"title": "Ad 2", "ad_id": 2, "author": "Author 2", "views_count": 20, "position": 2},
            {"title": "Ad 3", "ad_id": 3, "author": "Author 3", "views_count": 30, "position": 3},
            {"title": "Ad 4", "ad_id": 4, "author": "Author 4", "views_count": 40, "position": 4},
            {"title": "Ad 5", "ad_id": 5, "author": "Author 5", "views_count": 50, "position": 5},
            {"title": "Ad 6", "ad_id": 6, "author": "Author 6", "views_count": 60, "position": 6},
            {"title": "Ad 7", "ad_id": 7, "author": "Author 7", "views_count": 70, "position": 7},
            {"title": "Ad 8", "ad_id": 8, "author": "Author 8", "views_count": 80, "position": 8},
            {"title": "Ad 9", "ad_id": 9, "author": "Author 9", "views_count": 90, "position": 9},
            {"title": "Ad 10", "ad_id": 10, "author": "Author 10", "views_count": 100, "position": 10},
        ]

        for ad in ads:
            Ad.objects.create(**ad)

        self.stdout.write(self.style.SUCCESS('Successfully populated ads data'))

        # Create superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
            self.stdout.write(self.style.SUCCESS('Superuser created'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))
