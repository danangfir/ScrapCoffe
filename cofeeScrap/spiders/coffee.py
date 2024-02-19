import scrapy
from scrapy_selenium import SeleniumRequest

class CoffeeSpider(scrapy.Spider):
    name = 'coffeeSpider'
    
    def start_requests(self):
        url = "https://arutalacoffee.com/id/products?categories=products"
        yield SeleniumRequest(url=url, callback=self.parse, wait_time=10)

    def parse(self, response):
        # Misalnya struktur kelas yang benar ditemukan
        products = response.css('.Product_product_container__2k_HK .product_container')  
        for product in products:
            # Contoh perbaikan selektor
            url = product.css('a::attr(href)').get()  # Memperbaiki selektor untuk mendapatkan atribut href
            image = product.css('img::attr(src)').get()  # Memperbaiki selektor untuk mendapatkan atribut src
            name = product.css('.Product_product_title__2K0Ov::text').get().strip()  # Perbaikan selektor dan penggunaan ::text
            price = product.css('.Product_product_priceText__3HUZ5::text').get().strip()  # Perbaikan selektor dan penggunaan ::text

            yield {
                "url": response.urljoin(url),  # Memastikan URL lengkap
                "image": image,
                "name": name,
                "price": price,
            }



