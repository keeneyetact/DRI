# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import ImdbTvSerie

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['http://imdb.com/search/title?title_type=tv_series']
    custom_settings = {
        "HTTPCACHE_ENABLED":True,
    }

    def parse(self, response):
        for tv_serie in response.css('.lister-item'):
            try:
                content = tv_serie.css(".lister-item-content")

                rate = content.css('.ratings-imdb-rating::attr(data-value)').extract_first()
                title = content.css("h3 a::text").extract_first()
                rank, year = content.css("h3 span::text").extract()[:2]
                duration, genre = [content.css(".text-muted span::text").extract()[i] for i in[2,4]]
                description = content.css(".text-muted::text").extract()[-2]

                image = tv_serie.css(".lister-item-image a img")

                id = image.css("::attr(data-tconst)").extract_first()

                tv_serie_link = content.css("h3 a::attr(href)").extract_first()
                tv_serie_link = response.urljoin(tv_serie_link)

                data = {
                    "IMDB_id":id,
                    "rate":rate,
                    "popularity_rank":rank,
                    "title":title,
                    "year":year,
                    "duration":duration,
                    "genre":genre,
                    "recommandations":self.get_more(response),
                    "description":description
                }
                yield Request(tv_serie_link, callback=self.get_more, meta={"infos":data})

            except:
                pass

        next_url = response.xpath('//*[@id="main"]/div/div[1]/div[2]/a')[-1].css('::attr(href)').extract_first()
        link = response.urljoin(next_url)
        yield Request(link, callback=self.parse)


    def get_more(self,response):
        new_data = response.meta.get("infos").copy()
        new_data["recommandations"] = []

        try:
            for recom in response.xpath('//*[@id="title_recs"]/div[1]/div/div[2]').css('.rec_item'):
                id = recom.css('::attr(data-tconst)').extract_first()
                new_data["recommandations"].append(id)
        except:
            pass

        new_data["storyline"] = response.xpath('//*[@id="titleStoryLine"]/div[1]/p/span').css('::text').extract_first()
        new_data["image_url"] = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[4]/div[1]/a/img').css('::attr(src)').extract_first()
        yield ImdbTvSerie(new_data)
