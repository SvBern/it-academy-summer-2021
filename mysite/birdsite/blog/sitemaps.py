from django.contrib.sitemaps import Sitemap
from .models import Bird


class BirdSitemap(Sitemap):

    def items(self):
        return Bird.objects.all()
