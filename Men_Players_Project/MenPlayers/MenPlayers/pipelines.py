# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class MenplayersDatabasePipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('IndianMenPlayers.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE if EXISTS player_details""")
        self.curr.execute("""create table player_details(
                        Name char(1000) primary key,
                        Picture_url char(1000),
                        Jersey char(1000),
                        URL char(1000),
                        Role char(1000),
                        Batting_style char(1000),
                        Bowling_style char(1000),
                        Facebook_url char(1000),
                        Twitter_url char(1000),
                        Instagram_url char(1000),
                        Date_of_birth char(1000),
                        Description char(10000)
                        );""")
        self.curr.execute("""DROP TABLE if EXISTS batting_test_records""")
        self.curr.execute("""create table batting_test_records(
                                Name char(1000),
                                Matches int,
                                Innings int,
                                Not_out int,
                                Runs int,
                                Highest_score int,
                                Average real,
                                Balls_faced int,
                                Strike_rate real,
                                Hundreds int,
                                Fifties int,
                                Fours int,
                                Sixes int,
                                Catches int,
                                Stumps int
                                );""")
        self.curr.execute("""DROP TABLE if EXISTS bowling_test_records""")
        self.curr.execute("""create table bowling_test_records(
                                Name char(1000),
                                Matches int,
                                Innings int,
                                Balls int,
                                Runs int,
                                Wickets int,
                                Best_bowling_per_match char(15),
                                Average real,
                                Economy real,
                                Strike_rate real,
                                four_wicket_haul int,
                                five_wicket_haul int
                                );""")
        self.curr.execute("""DROP TABLE if EXISTS batting_odi_records""")
        self.curr.execute("""create table batting_odi_records(
                                        Name char(1000),
                                        Matches int,
                                        Innings int,
                                        Not_out int,
                                        Runs int,
                                        Highest_score int,
                                        Average real,
                                        Balls_faced int,
                                        Strike_rate real,
                                        Hundreds int,
                                        Fifties int,
                                        Fours int,
                                        Sixes int,
                                        Catches int,
                                        Stumps int
                                        );""")
        self.curr.execute("""DROP TABLE if EXISTS bowling_odi_records""")
        self.curr.execute("""create table bowling_odi_records(
                                        Name char(1000),
                                        Matches int,
                                        Innings int,
                                        Balls int,
                                        Runs int,
                                        Wickets int,
                                        Best_bowling_per_match char(15),
                                        Average real,
                                        Economy real,
                                        Strike_rate real,
                                        four_wicket_haul int,
                                        five_wicket_haul int
                                        );""")
        self.curr.execute("""DROP TABLE if EXISTS batting_t20i_records""")
        self.curr.execute("""create table batting_t20i_records(
                                        Name char(1000),
                                        Matches int,
                                        Innings int,
                                        Not_out int,
                                        Runs int,
                                        Highest_score int,
                                        Average real,
                                        Balls_faced int,
                                        Strike_rate real,
                                        Hundreds int,
                                        Fifties int,
                                        Fours int,
                                        Sixes int,
                                        Catches int,
                                        Stumps int
                                        );""")
        self.curr.execute("""DROP TABLE if EXISTS bowling_t20i_records""")
        self.curr.execute("""create table bowling_t20i_records(
                                        Name char(1000),
                                        Matches int,
                                        Innings int,
                                        Balls int,
                                        Runs int,
                                        Wickets int,
                                        Best_bowling_per_match char(15),
                                        Average real,
                                        Economy real,
                                        Strike_rate real,
                                        four_wicket_haul int,
                                        five_wicket_haul int
                                        );""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into player_details values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (
            item['player_details']['player_name'],
            item['player_details']['player_picture'],
            item['player_details']['player_jersey'],
            item['player_details']['player_url'],
            item['player_details']['player_role'],
            item['player_details']['player_batting_style'],
            item['player_details']['player_bowling_style'],
            item['player_details']['player_facebook_link'],
            item['player_details']['player_twitter_link'],
            item['player_details']['player_instagram_link'],
            item['player_details']['player_dob'],
            item['player_details']['player_description']
        ))
        self.curr.execute("""insert into batting_test_records values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
                          (
                              item['player_details']['player_name'],
                              item['player_batting_test_records']['Mat'],
                              item['player_batting_test_records']['Inn'],
                              item['player_batting_test_records']['No'],
                              item['player_batting_test_records']['Runs'],
                              item['player_batting_test_records']['HS'],
                              item['player_batting_test_records']['Ave'],
                              item['player_batting_test_records']['BF'],
                              item['player_batting_test_records']['SR'],
                              item['player_batting_test_records']['100'],
                              item['player_batting_test_records']['50'],
                              item['player_batting_test_records']['4s'],
                              item['player_batting_test_records']['6s'],
                              item['player_batting_test_records']['CT'],
                              item['player_batting_test_records']['ST']
                          ))
        self.curr.execute("""insert into bowling_test_records values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
                          (
                              item['player_details']['player_name'],
                              item['player_bowling_test_records']['Mat'],
                              item['player_bowling_test_records']['Inn'],
                              item['player_bowling_test_records']['Balls'],
                              item['player_bowling_test_records']['Runs'],
                              item['player_bowling_test_records']['WKTS'],
                              item['player_bowling_test_records']['BBM'],
                              item['player_bowling_test_records']['Ave'],
                              item['player_bowling_test_records']['Econ'],
                              item['player_bowling_test_records']['SR'],
                              item['player_bowling_test_records']['4W'],
                              item['player_bowling_test_records']['5W']
                          ))
        self.curr.execute("""insert into batting_odi_records values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
                          (
                              item['player_details']['player_name'],
                              item['player_batting_odi_records']['Mat'],
                              item['player_batting_odi_records']['Inn'],
                              item['player_batting_odi_records']['No'],
                              item['player_batting_odi_records']['Runs'],
                              item['player_batting_odi_records']['HS'],
                              item['player_batting_odi_records']['Ave'],
                              item['player_batting_odi_records']['BF'],
                              item['player_batting_odi_records']['SR'],
                              item['player_batting_odi_records']['100'],
                              item['player_batting_odi_records']['50'],
                              item['player_batting_odi_records']['4s'],
                              item['player_batting_odi_records']['6s'],
                              item['player_batting_odi_records']['CT'],
                              item['player_batting_odi_records']['ST']
                          ))
        self.curr.execute("""insert into bowling_odi_records values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
                          (
                              item['player_details']['player_name'],
                              item['player_bowling_odi_records']['Mat'],
                              item['player_bowling_odi_records']['Inn'],
                              item['player_bowling_odi_records']['Balls'],
                              item['player_bowling_odi_records']['Runs'],
                              item['player_bowling_odi_records']['WKTS'],
                              item['player_bowling_odi_records']['BBM'],
                              item['player_bowling_odi_records']['Ave'],
                              item['player_bowling_odi_records']['Econ'],
                              item['player_bowling_odi_records']['SR'],
                              item['player_bowling_odi_records']['4W'],
                              item['player_bowling_odi_records']['5W']
                          ))
        self.curr.execute("""insert into batting_t20i_records values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
                          (
                              item['player_details']['player_name'],
                              item['player_batting_t20i_records']['Mat'],
                              item['player_batting_t20i_records']['Inn'],
                              item['player_batting_t20i_records']['No'],
                              item['player_batting_t20i_records']['Runs'],
                              item['player_batting_t20i_records']['HS'],
                              item['player_batting_t20i_records']['Ave'],
                              item['player_batting_t20i_records']['BF'],
                              item['player_batting_t20i_records']['SR'],
                              item['player_batting_t20i_records']['100'],
                              item['player_batting_t20i_records']['50'],
                              item['player_batting_t20i_records']['4s'],
                              item['player_batting_t20i_records']['6s'],
                              item['player_batting_t20i_records']['CT'],
                              item['player_batting_t20i_records']['ST']
                          ))
        self.curr.execute("""insert into bowling_t20i_records values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
                          (
                              item['player_details']['player_name'],
                              item['player_bowling_t20i_records']['Mat'],
                              item['player_bowling_t20i_records']['Inn'],
                              item['player_bowling_t20i_records']['Balls'],
                              item['player_bowling_t20i_records']['Runs'],
                              item['player_bowling_t20i_records']['WKTS'],
                              item['player_bowling_t20i_records']['BBM'],
                              item['player_bowling_t20i_records']['Ave'],
                              item['player_bowling_t20i_records']['Econ'],
                              item['player_bowling_t20i_records']['SR'],
                              item['player_bowling_t20i_records']['4W'],
                              item['player_bowling_t20i_records']['5W']
                          ))
        self.conn.commit()
