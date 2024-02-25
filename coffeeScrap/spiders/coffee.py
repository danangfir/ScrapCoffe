import scrapy
from coffeeScrap.items import Coffeeitem

class coffeeSpider(scrapy.Spider):
    name = "coffeeScrap"
    
    def start_requests(self):
            url = "https://arutalacoffee.com/id/products?categories=products"
            yield scrapy.Request(url, meta={'playwright': True})
        
    def parse(self, response):
            for coffee in response.css('Product_product_labelContainer__16LVk'):
                coffee_item = Coffeeitem()
                coffee_item['text'] = coffee.css('p.Product_product_title__2K0Ov::text').get()
                coffee_item['tags'] = coffee.css('div.productCategory-categoryNameClassName::text').get()
                coffee_item['price'] = coffee.css('p.Product_product_price__1_5Ly').get()
                yield coffee_item
        
        
        