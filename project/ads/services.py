from .models import Ad


class AdService:
    @staticmethod
    def get_ad_by_id(ad_id):
        try:
            return Ad.objects.get(ad_id=ad_id)
        except Ad.DoesNotExist:
            return None

    @staticmethod
    def create_ad(data):
        ad = Ad.objects.create(**data)
        return ad

    @staticmethod
    def update_ad(ad_id, data):
        ad = AdService.get_ad_by_id(ad_id)
        if ad:
            for key, value in data.items():
                setattr(ad, key, value)
            ad.save()
            return ad
        return None

    @staticmethod
    def delete_ad(ad_id):
        ad = AdService.get_ad_by_id(ad_id)
        if ad:
            ad.delete()
            return True
        return False
