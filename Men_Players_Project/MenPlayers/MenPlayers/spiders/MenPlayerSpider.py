import scrapy
from ..items import MenplayersItem
import os
import requests

class MenplayerspiderSpider(scrapy.Spider):
    name = 'MenPlayerSpider'
    allowed_domains = ['www.bcci.tv']
    start_urls = ['https://www.bcci.tv/players/men']

    def parse(self, response):
        player_urls = response.css('.player-card a::attr(href)').extract()
        for url in player_urls:
            yield response.follow(url, callback=self.parse_records)

    def parse_records(self, response):
        players = MenplayersItem()

        details = {}
        batting_TEST = {}
        batting_ODI = {}
        batting_T20I = {}
        bowling_TEST = {}
        bowling_ODI = {}
        bowling_T20I = {}

        details['player_name'] = response.css('h3::text').get().capitalize() + response.css(
            '.profile-name span::text').get().capitalize()
        details['player_picture'] = response.css('.px-5 > img::attr(src)').get()
        details['player_jersey'] = response.css('.j-no ::text').get()
        details['player_url'] = response.url
        details['player_role'] = response.css('.align-items-center:nth-child(1)>h4::text').get()
        details['player_batting_style'] = response.css('.align-items-center:nth-child(2)>h4::text').get()
        details['player_bowling_style'] = response.css('.align-items-center:nth-child(3)>h4::text').get()
        details['player_facebook_link'] = response.css('.player-social li:nth-child(1) a::attr(href)').get()
        details['player_twitter_link'] = response.css('.player-social li:nth-child(2) a::attr(href)').get()
        details['player_instagram_link'] = response.css('.player-social li:nth-child(3) a::attr(href)').get()
        details['player_dob'] = response.css('.align-items-center.mb-0 h4::text').get().strip()
        details['player_description'] = response.css('.flex-column p::text').get().strip()

        keys = response.css('th+ th::text').extract()
        test_values = response.css('.t-test td+ td::text').extract()
        for i in range(len(keys)):
            if i < 14:
                batting_TEST[keys[i]] = test_values[i]
            else:
                bowling_TEST[keys[i]] = test_values[i]
        odi_values = response.css('.t-odi td+ td::text').extract()
        for i in range(len(keys)):
            if i < 14:
                batting_ODI[keys[i]] = odi_values[i]
            else:
                bowling_ODI[keys[i]] = odi_values[i]
        t20i_values = response.css('.t-t20i td+ td::text').extract()
        for i in range(len(keys)):
            if i < 14:
                batting_T20I[keys[i]] = t20i_values[i]
            else:
                bowling_T20I[keys[i]] = t20i_values[i]

        # Downloading Profile Picture
        name = details['player_name']
        link = details['player_picture']
        file_type = link.split('.')[-1]
        file_name = name + '.' + file_type
        basic_path = "J:\\WEB SCRAPING PROJECTS\\BCCI\\Men_Players_Project\\MenPlayers\\images"
        image_path = os.path.join(basic_path, file_name)
        img_response = requests.get(link)
        with open(image_path, "wb") as img:
            img.write(img_response.content)

        players['player_details'] = details
        players['player_batting_test_records'] = batting_TEST
        players['player_batting_odi_records'] = batting_ODI
        players['player_batting_t20i_records'] = batting_T20I
        players['player_bowling_test_records'] = bowling_TEST
        players['player_bowling_odi_records'] = bowling_ODI
        players['player_bowling_t20i_records'] = bowling_T20I

        return players

        # Printing Block
        # print("-"*122)
        # print("-"*47 + " Batting and Fielding Stats " + "-"*47)
        # print("-"*122)
        # print("         ", end="\t")
        # for i in range(len(keys)):
        #     if i < 14:
        #         print(keys[i], end="\t")
        # print()
        # print("   TEST   ", end="\t")
        # for i in range(len(keys)):
        #     if i < 14:
        #         print(batting_TEST[keys[i]], end="\t")
        # print()
        # print("   ODI   ", end="\t")
        # for i in range(len(keys)):
        #     if i < 14:
        #         print(batting_ODI[keys[i]], end="\t")
        # print()
        # print("   T20I   ", end="\t")
        # for i in range(len(keys)):
        #     if i < 14:
        #         print(batting_T20I[keys[i]], end="\t")
        # print()
        # print("-" * 98)
        # print("-" * 41 + " Bowling Stats " + "-" * 42)
        # print("-" * 98)
        # print("         ", end="\t")
        # for i in range(len(keys)):
        #     if i >= 14:
        #         print(keys[i], end="\t")
        # print()
        # print("   TEST   ", end="\t")
        # for i in range(len(keys)):
        #     if i >= 14:
        #         print(bowling_TEST[keys[i]], end="\t")
        # print()
        # print("   ODI   ", end="\t")
        # for i in range(len(keys)):
        #     if i >= 14:
        #         print(bowling_ODI[keys[i]], end="\t")
        # print()
        # print("   T20I   ", end="\t")
        # for i in range(len(keys)):
        #     if i >= 14:
        #         print(bowling_T20I[keys[i]], end="\t")
        # print()