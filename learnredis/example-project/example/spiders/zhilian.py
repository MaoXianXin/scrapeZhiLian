# -*- coding:utf8 -*-
from scrapy_redis.spiders import RedisSpider
import scrapy
import re

class MySpider(RedisSpider):
	name = "zhilian"
	redis_key = "zhilian:start_urls"
	allowed_domains = ["jobs.zhaopin.com","sou.zhaopin.com"]
	#处理每种职业的页面
	def parse(self,response):
		print(response.url)
		pagenum = response.xpath("//body/div[3]/div[3]/div[2]/form/div[1]/div[1]/div[3]/ul/li[6]/a/text()").extract_first()
		if int(pagenum) <= 30:
			jobsurl = response.css("td.zwmc>div>a::attr(href)").extract()
			for joburl in jobsurl:
				yield scrapy.Request(joburl,callback=self.parsejob)
			nextPage = response.xpath("//body/div[3]/div[3]/div[2]/form/div[1]/div[1]/div[3]/ul/li[11]/a/@href").extract_first()
			yield scrapy.Request(nextPage,callback=self.parse)
	#提取页面中的工作详细信息
	def parsejob(self,response):
		companylatitudeandlongitude = response.xpath("//body/div[6]/div[1]/div[1]/div/div[1]/h2/a/@href").extract_first()
		if companylatitudeandlongitude is not None:
			latitudeandlongitude = response.xpath("//body/div[6]/div[1]/div[1]/div/div[1]/h2/a/@href").re(r"(\d+)")
#			print(latitudeandlongitude)
			longitude = latitudeandlongitude[0] + "." + latitudeandlongitude[1]
			latitude = latitudeandlongitude[2] + "." + latitudeandlongitude[3]
#			print(latitude)
#			print(longitude)
			yield {
				'jobname':response.xpath("//body/div[5]/div[1]/div[1]/h1/text()").extract_first(),
				'salary':response.xpath("//body/div[6]/div[1]/ul/li[1]/strong/text()").extract_first(),
				'workplace':response.xpath("//body/div[6]/div[1]/ul/li[2]/strong/a/text()").extract_first(),
				'releasetime':response.xpath("//span[@id='span4freshdate']/text()").extract_first(),
				'experience':response.xpath("//body/div[6]/div[1]/ul/li[5]/strong/text()").extract_first(),
				'education':response.xpath("//body/div[6]/div[1]/ul/li[6]/strong/text()").extract_first(),
				'neednum':response.xpath("//body/div[6]/div[1]/ul/li[7]/strong/text()").extract_first(),
				'jobcategory':response.xpath("//body/div[6]/div[1]/ul/li[8]/strong/a/text()").extract_first(),
				'companyaddrurl':response.xpath("//body/div[5]/div[1]/div[1]/h2/a/@href").extract_first(),
				'latitude':latitude,
				'longitude':longitude,
			}
