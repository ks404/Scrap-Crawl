from dynamic_scraper.spiders.django_spider import DjangoSpider
from metalapp.models import Listing, SearchTerm, ListingItem


class ListingSpider(DjangoSpider):
    
    name = 'listing_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(SearchTerm, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Listing
        self.scraped_obj_item_class = ListingItem
        super(ListingSpider, self).__init__(self, *args, **kwargs)

#erase **kwargs in line 9 and 16