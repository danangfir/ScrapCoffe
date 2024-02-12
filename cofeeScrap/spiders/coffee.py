import scrapy
import asyncio 
from playwright.async_api import Playwright, async_playwright

class CoffeeSpider(scrapy.Spider):
    name = 'coffeSpider'
    allowed_domains = ['https://fore.coffee/id/']
    start_urls = ['https://fore.coffee/id/menu-indo/']
    
    def parse(self, response):
        pass
    
    
    
    
    
    