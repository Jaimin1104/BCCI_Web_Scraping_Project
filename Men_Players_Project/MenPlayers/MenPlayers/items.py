# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MenplayersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    player_details = scrapy.Field()
    player_batting_test_records = scrapy.Field()
    player_batting_odi_records = scrapy.Field()
    player_batting_t20i_records = scrapy.Field()
    player_bowling_test_records = scrapy.Field()
    player_bowling_odi_records = scrapy.Field()
    player_bowling_t20i_records = scrapy.Field()
