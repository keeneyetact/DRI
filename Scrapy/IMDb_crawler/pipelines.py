# -*- coding: utf-8 -*-
import pymongo

class MongoPipeline(object):

    collection_name = 'tv_series'
    #collection_name = 'trucbidon'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient()
        self.db = self.client["test"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item

class TextPipeline(object):

    def process_item(self, item, spider):
        for key in ['genre','description','title','storyline']:
            if item[key]:
                item[key] = self.clean(item[key])
        if item['popularity_rank']:
            item['popularity_rank'] = item['popularity_rank'].replace('.','')
        if item['IMDB_id']:
            item['IMDB_id'] = item['IMDB_id'].replace('tt','')
        if item['recommandations']:
            item['recommandations'] = [i.replace('tt','') for i in item['recommandations']]
        return item
        #else: raise

    def clean(self,string_):
        cleaned = string_.replace("\n",'')
        if cleaned is not None:
            return " ".join(cleaned.split())
