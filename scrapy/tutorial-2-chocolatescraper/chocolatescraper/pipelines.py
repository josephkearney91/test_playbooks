# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ChocolatescraperPipeline:
    def process_item(self, item, spider):
        return item



class PriceToUSDPipeline:

    gbpToUsdRate = 1.3

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('price'):
                        #converting the price to a float
            floatPrice = float(adapter['price'])
            #converting the price from gbp to usd using our hard coded exchange rate
            usdConvertedPrice = str('{:.2f}'.format(floatPrice * self.gbpToUsdRate))
            #adding the dollar sign to the front of the price
            adapter['price'] = '$' + usdConvertedPrice 
            return item
        else:
            raise DropItem(f"Missing price in {item}")
