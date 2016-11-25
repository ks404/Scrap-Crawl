from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
#from scrapy.contrib.djangoitem import DjangoItem
from scrapy_djangoitem import DjangoItem
from dynamic_scraper.models import Scraper, SchedulerRuntime





class SearchTerm (models.Model):
	title = models.CharField ( blank = True, max_length = 2000 )
	url = models.URLField()
	scraper = models.ForeignKey ( Scraper, blank = True, null = True, on_delete = models.SET_NULL )
	scraper_runtime = models.ForeignKey ( SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return self.title


class Listing (models.Model):
	material = models.CharField (blank = True, max_length = 2000)
	weight = models.CharField (null = True, max_length = 2000 )
	location = models.CharField (blank = True, max_length = 2000)
	closing = models.CharField (blank = True, max_length = 2000)
	link = models.CharField (blank = True , max_length = 2000)
	price = models.CharField (blank = True , max_length = 2000)
	search_term = models.ForeignKey(SearchTerm)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

	def __unicode__(self):
		return self.material


class ListingItem (DjangoItem):
	django_model = Listing

