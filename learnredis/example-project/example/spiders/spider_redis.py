from scrapy_redis.spiders import RedisSpider
import scrapy

class MySpider(RedisSpider):
	name = 'myspider_redis1'
	redis_key = 'myspider:start_urls'
	allowed_domains = ['jobs.zhaopin.com','sou.zhaopin.com']
	def parse(self, response):
		for job in response.css('td.zwmc>div>a'):
			joburl = job.css('a::attr("href")').extract_first()
			joburl = response.urljoin(joburl)
			print(joburl)
			yield scrapy.Request(joburl,callback=self.parse_job)
		next_page = response.css('a.next-page::attr("href")').extract_first()
		next_page = response.urljoin(next_page)
		if next_page is not None:
			yield scrapy.Request(next_page,callback=self.parse)
	def parse_job(self,response):
		yield {
			'jobname':response.xpath("//body/div[5]/div[1]/div[1]/h1/text()").extract_first(),
			'companyaddrurl':response.xpath("//body/div[5]/div[1]/div[1]/h2/a/@href").extract_first(),
			'salary':response.xpath("//body/div[6]/div[1]/ul/li[1]/strong/text()").extract_first(),
			'jobdate':response.xpath("//span[@id='span4freshdate']/text()").extract_first(),
			'exp':response.xpath("//body/div[6]/div[1]/ul/li[5]/strong/text()").extract_first(),
			'education':response.xpath("//body/div[6]/div[1]/ul/li[6]/strong/text()").extract_first(),
		}
