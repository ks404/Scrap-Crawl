# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


#class ScrapyprojectPipeline(object):
 #   def process_item(self, item, spider):
  #      return item




from django.db.utils import IntegrityError
from scrapy import log
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime

class DjangoWriterPipeline(object):

    def process_item(self, item, spider):
        #for i in item['search_term']:
        try:
            item['search_term'] = spider.ref_object

            checker_rt = SchedulerRuntime(runtime_type='C')
            checker_rt.save()
            item['checker_runtime'] = checker_rt

            item.save()
            spider.action_successful = True
            spider.log("Item saved.", log.INFO)

        except IntegrityError, e:
            spider.log(str(e), log.ERROR)
            raise DropItem("Missing attribute.")

        return item