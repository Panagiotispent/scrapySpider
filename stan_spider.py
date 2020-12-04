# -*- coding: utf-8 -*-
import scrapy

class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'https://github.com/stan-dev/example-models',
    ]
    
    
    def parse(self, response):
        for stan_file in response.css("td.content"):
            titles= stan_file.css('.js-navigation-open::text').getall()
            
            if '.stan' in (str(titles)):
                yield {
                'title': stan_file.css('.js-navigation-open::text').get()
            }
	
        for href in response.css('.js-navigation-open::attr(href)'):
        	yield response.follow(href, callback=self.parse)
            
