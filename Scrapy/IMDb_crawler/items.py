# -*- coding =  utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in =
# https = //doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ImdbTvSerie(scrapy.Item):
    IMDB_id = scrapy.Field()
    rate = scrapy.Field()
    popularity_rank = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    image_url = scrapy.Field()
    duration = scrapy.Field()
    genre = scrapy.Field()
    recommandations = scrapy.Field()
    description = scrapy.Field()
    recommandations = scrapy.Field()
    storyline = scrapy.Field()
