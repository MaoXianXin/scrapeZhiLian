# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class ExampleItem(Item):
	jobname = Field()
	salary = Field()
	workplace = Field()
	releasetime = Field()
	experience = Field()
	education = Field()
	neednum = Field()
	jobcategory = Field()
	crawled = Field()
	spider = Field()
	companyaddrurl = Field()
	companylatitudeandlongitude = Field()
	latitude = Field()
	longitude = Field()
	
        description = Field()
        link = Field()
        url = Field()
	joburl = Field()
	companyaddr = Field()
	jobdate = Field()
	exp = Field()
	education = Field()
	jobaddr = Field()


class ExampleLoader(ItemLoader):
        default_item_class = ExampleItem
        default_input_processor = MapCompose(lambda s: s.strip())
        default_output_processor = TakeFirst()
        description_out = Join()
