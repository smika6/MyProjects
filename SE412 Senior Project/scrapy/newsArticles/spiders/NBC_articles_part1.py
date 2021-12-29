# https://docs.scrapy.org/en/latest/intro/newsArticles.html
# https://www.pythonnewsArticles.net/python-basics/python-write-csv-file/
# https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html#extracting-articles
# https://stackoverflow.com/questions/56677636/how-to-use-newspaper3k-library-without-downloading-articles

import scrapy
import os
import newspaper
import csv
import json
import time



# def createCSV():
# 	header = ['Source Name', 'Related Story', 'Title', 'Text', 'URL']
# 	cwd = os.getcwd()
# 	csvName = "articles3.csv"
# 	midpath = "newsArticles"
# 	csv_path = "csv"
# 	csvFile = os.path.join(cwd, midpath, csv_path, csvName)
#
# 	with open(csvFile, 'w', encoding='UTF8', newline='') as f:
# 		writer = csv.writer(f)
#
# 		# write the header
# 		writer.writerow(header)



def addToCSV(data):
	cwd = os.getcwd()
	csvName = "articles.csv"
	midpath = "newsArticles"
	csv_path = "csv"
	csvFile = os.path.join(cwd, midpath, csv_path, csvName)

	with open(csvFile, 'a', encoding='UTF8', newline='') as f:
		writer = csv.writer(f)

		# write the data
		writer.writerow(data)




class QuotesSpider(scrapy.Spider):
	name = "nbc1"

	def start_requests(self):
		# createCSV()
		json = {
			"source": [
				"NBC",
				"NBC",
				"NBC",
				"NBC",
				"NBC",
				"NBC",
				"NBC",
				"NBC",
				"NBC",
				"NBC",
				"NBC",
				"NBC",
				"NBC",
				"NBC",
				"NBC",
				"NBC"

			],
			"relatedStories": [
				"Hurricane Katrina",
				"Hussein Executed",
				"House Speaker",
				"Obama Elected",
				"Swine Flu",
				"Japan Earthquake & Tsunamis",
				"London Olympics ",
				"Boston Marathon Bombings",
				"Russia Invades Ukraine",
				"Gay Marriage ",
				"Trump Elected",
				"Trump Inauguration",
				"Brett Kavanaugh picked for SCJ",
				"Area 51 Raid",
				"George Floyd Death",
				"January 6th"
			],
			"urls": [
				"https://www.nbcnews.com/id/wbna9269337",
				"https://www.nbcnews.com/id/wbna16389128",
				"https://www.nbcnews.com/id/wbna16449288",
				"https://www.nbcdfw.com/news/politics/decision_day/2112662/",
				"https://www.nbcnews.com/id/wbna33239736",
				"https://www.nbcnews.com/id/wbna42044293",
				"https://nbcsportsgrouppressbox.com/2012/08/12/through-16-days-31-1-million-average-primetime-viewership-for-london-olympics-on-nbc-is-best-for-non-u-s-summer-olympics-in-36-years/",
				"https://www.nbcnews.com/slideshow/amp/boston-marathon-bombing-51547100",
				"https://www.nbcnews.com/storyline/ukraine-crisis/what-invasion-russian-denials-crimea-trigger-war-words-n45666",
				"https://www.nbcnews.com/news/us-news/same-sex-marraige-legal-nationwide-supreme-court-rules-n375551",
				"https://www.cnbc.com/2016/11/08/live-2016-election-day-results-donald-trump-and-hillary-clinton-race-to-the-white-house.html",
				"https://www.nbcnews.com/storyline/inauguration-2017/trump-inauguration-what-world-s-saying-about-next-president-n709456",
				"https://www.nbcnews.com/politics/supreme-court/who-supreme-court-nominee-brett-kavanaugh-n890071",
				"https://www.nbcnews.com/think/opinion/storming-area-51-september-20-here-s-why-you-re-ncna1034781",
				"https://www.nbcnews.com/news/us-news/man-dies-after-pleading-i-can-t-breathe-during-arrest-n1214586",
				"https://www.nbcnews.com/politics/congress/blog/2021-01-06-congress-electoral-vote-count-n1253179"
			]
		}

		for i, url in enumerate(json["urls"]):
			yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(source=json["source"][i], relatedStory=json["relatedStories"][i]))



	def parse(self, response, source, relatedStory):
		data = []
		article = newspaper.Article(url = ' ')
		article.set_html(response.body)
		article.parse()
		# print('TITLE: ', article.title)
		# print(source)
		# print(relatedStory)
		data.append(source)
		data.append(relatedStory)
		data.append(article.title)
		data.append(article.text)
		data.append(response.url)
		addToCSV(data)
