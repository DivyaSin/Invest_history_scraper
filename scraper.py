# How to run: scrapy runspider [file-name] -o [output-file-format]
# Example: scrapy runspider scraper.py -o invest_history.csv

import scrapy
from scrapy.item import Item, Field

# This function creates items in our spider item class.
class InvestHistory(Item):
	date = Field()
	price = Field()
	opening = Field()
	high = Field()
	low = Field()
	vol = Field()
	change = Field()
	commodity = Field()

# This function takes url and parses each url. It returns the items in one file.
class InvestSpider(scrapy.Spider):
	name = 'investspider'
	start_urls = ["https://www.investing.com/commodities/gold-historical-data", "https://www.investing.com/commodities/silver-historical-data"]

	def parse(self, response):
		items =[]
		commodity = (response.url.split('/')[-1]).split('-')[-3]
		rows = response.xpath('//table[@id="curr_table"]/tbody/tr')
		for row in rows:
			item = InvestHistory()
			item['date']=row.xpath('td[1]/text()').extract()
			item['price']=row.xpath('td[2]/text()').extract()
			item['opening']=row.xpath('td[3]/text()').extract()
			item['high']=row.xpath('td[4]/text()').extract()
			item['low']=row.xpath('td[5]/text()').extract()
			item['vol']=row.xpath('td[6]/text()').extract()
			item['change']=row.xpath('td[7]/text()').extract()
			item['commodity']=commodity
			items.append(item)
		return items

        	



