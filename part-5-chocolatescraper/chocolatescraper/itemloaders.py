from itemloaders.processors import TakeFirst, Compose, MapCompose
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags


class ChocolateProductLoader(ItemLoader):

    default_output_processor = TakeFirst()

    price_in = MapCompose(lambda x: x.split("£")[-1])
    url_in = MapCompose(lambda x: 'https://www.chocolate.co.uk' + x )

