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
# 	csvName = "articles2.csv"
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
	name = "fox1"

	def start_requests(self):
		# createCSV()
		json = {
			"source": [
				"Fox News",
				"Fox News",
				"Fox News",
				"Fox News",
				"Fox News",
				"Fox News",
				"Fox News",
				"Fox News",
				"Fox News",
				"Fox News",
				"Fox News",
				"Fox News",
				"Fox News",
				"Fox News",
				"Fox News",
				"Fox News"
			],
			"relatedStories": [
				"Hurricane Katrina",
				"Hussein Executed",
				"Obama Elected",
				"Swine Flu",
				"BP Oil Spill",
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
				"https://www.foxnews.com/story/keeping-the-record-straight-on-the-katrina-story",
				"https://www.foxnews.com/story/saddam-hussein-executed-by-hanging-in-iraq",
				"https://www.foxnews.com/story/fox-news-exit-poll-summary",
				"https://www.foxnews.com/story/government-to-intensely-track-for-h1n1-shot-side-effects",
				"https://www.foxnews.com/us/bp-spill-response-plans-severely-flawed",
				"https://www.foxnews.com/world/hundreds-of-bodies-found-in-japan-after-massive-tsunami-spawned-by-earthquake",
				"https://www.foxnews.com/sports/london-2012-closing-ceremony-rio-de-janeiro-takes-torch-as-britain-closes-with-rock-roll-extravaganza",
				"https://www.foxnews.com/us/3-dead-more-than-130-injured-as-2-bombs-explode-near-boston-marathon-finish-line",
				"https://www.foxnews.com/world/ukraine-official-russia-has-launched-armed-invasion-in-crimea",
				"https://www.foxnews.com/opinion/gay-marriage-why-supreme-court-got-it-wrong",
				"https://www.foxnews.com/politics/trump-wins-presidency-defeats-clinton-in-historic-election-upset",
				"https://www.foxnews.com/us/fact-check-trump-overstates-crowd-size-at-inaugural",
				"https://www.foxnews.com/politics/trump-nominates-brett-kavanaugh-to-supreme-court",
				"https://www.foxnews.com/science/storm-area-51-raid-alien-community-believers-las-vegas",
				"https://www.foxnews.com/us/police-protesters-clash-thousands-demonstrate-minnesota-streets-over-death-george-floyd",
				"https://www.foxnews.com/politics/how-wednesdays-capitol-riot-come-to-fruition",
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
