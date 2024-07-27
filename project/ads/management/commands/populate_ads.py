from django.core.management.base import BaseCommand

from ....ads.models import Ad


class Command(BaseCommand):
    help = 'Populate ads data'

    def handle(self, *args, **kwargs):
        ads = [
            {"title": "Ad 1", "ad_id": 1, "author": "Author 1", "views_count": 100, "position": 1},
            {"title": "Ad 2", "ad_id": 2, "author": "Author 2", "views_count": 200, "position": 2},
            {"title": "Ad 3", "ad_id": 3, "author": "Author 3", "views_count": 300, "position": 3},
            {"title": "Ad 4", "ad_id": 4, "author": "Author 4", "views_count": 400, "position": 4},
            {"title": "Ad 5", "ad_id": 5, "author": "Author 5", "views_count": 500, "position": 5},
            {"title": "Ad 6", "ad_id": 6, "author": "Author 6", "views_count": 600, "position": 6},
            {"title": "Ad 7", "ad_id": 7, "author": "Author 7", "views_count": 700, "position": 7},
            {"title": "Ad 8", "ad_id": 8, "author": "Author 8", "views_count": 800, "position": 8},
            {"title": "Ad 9", "ad_id": 9, "author": "Author 9", "views_count": 900, "position": 9},
            {"title": "Ad 10", "ad_id": 10, "author": "Author 10", "views_count": 1000, "position": 10},
        ]

        for ad_data in ads:
            ad, created = Ad.objects.get_or_create(ad_id=ad_data["ad_id"], defaults=ad_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created ad: {ad.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Ad already exists: {ad.title}'))
