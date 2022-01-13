import scrapy
from chocolatescraper.itemloaders import ChocolateProductLoader
from chocolatescraper.items import ChocolateProduct  

class ChocolateSpider(scrapy.Spider):

   #the name of the spider
   name = 'chocolatespider'

   #these are the urls that we will start scraping
   start_urls = ['https://www.chocolate.co.uk/collections/all']

   def parse(self, response):

       products = response.css('product-item')
       for product in products:
           #here we put the data returned into the format we want to output for our csv or json file
           #try:
           chocolate = ChocolateProductLoader(item=ChocolateProduct(), selector=product)

           print('**** making a chocolate ****')    
           chocolate.add_css('name', "a.product-item-meta__title::text")
           chocolate.add_css('price', 'span.price', re='<span class="price">\n              <span class="visually-hidden">Sale price</span>(.*)</span>')
           chocolate.add_css('url', 'div.product-item-meta a::attr(href)')

           yield chocolate.load_item()

           #except:
            #   yield{
             #      'name' : product.css('a.product-item-meta__title::text').get(),
              #     'price' : 'sold out',
               #    'url' : product.css('div.product-item-meta a').attrib['href'],
               #}

       next_page = response.css('[rel="next"] ::attr(href)').get()

       if next_page is not None:
           next_page_url = 'https://www.chocolate.co.uk' + next_page
           yield response.follow(next_page_url, callback=self.parse)
