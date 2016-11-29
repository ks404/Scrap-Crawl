from django.shortcuts import render

from django.http import HttpResponse
from models import Listing, SearchTerm

from django.template import RequestContext, loader

from subprocess import call #lets your run commandline

# Create your views here.

def copper(request):

	# deleted '-a id=1' before -a do action
	call(['scrapy crawl listing_spider -a do_action=yes '], stdin=None, stdout=None, stderr=None, shell=True)

	#works with shell=true, but not false. Why?

	#scrapy crawl listing_spider -a id=1 -a do_action=yes

	template = loader.get_template('metalapp/copper.html')
	
	outtable = Listing.objects.filter( search_term__title = 'copper')

	context = RequestContext (request, {'outtable': outtable })

	return HttpResponse(template.render(context))

def alluminum(request):

	
	call(['scrapy crawl listing_spider -a do_action=yes '], stdin=None, stdout=None, stderr=None, shell=True)

	template = loader.get_template('metalapp/alluminum.html')
	
	outtable = Listing.objects.filter ( search_term__title = 'alluminum')

	context = RequestContext (request, {'outtable': outtable })

	return HttpResponse(template.render(context))

def stainless(request):

	
	call(['scrapy crawl listing_spider -a id=4 -a do_action=yes '], stdin=None, stdout=None, stderr=None, shell=True)

	template = loader.get_template('metalapp/stainless.html')
	
	outtable = Listing.objects.filter( search_term__title = 'stainless' )

	context = RequestContext (request, {'outtable': outtable })

	return HttpResponse(template.render(context))

def shells(request):

	
	call(['scrapy crawl listing_spider -a id=5 -a do_action=yes '], stdin=None, stdout=None, stderr=None, shell=True)

	template = loader.get_template('metalapp/shells.html')
	
	outtable = Listing.objects.filter( search_term__title = 'shells' )

	context = RequestContext (request, {'outtable': outtable })

	return HttpResponse(template.render(context))

def index(request):

	outtable = Listing.objects.all()

	context = RequestContext (request, {'outtable': outtable })

	template = loader.get_template('metalapp/index.html')

	return HttpResponse(template.render(context))

