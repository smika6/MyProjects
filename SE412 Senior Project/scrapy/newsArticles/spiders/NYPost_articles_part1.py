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
# 	csvName = "articles4.csv"
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
	name = "nyp1"

	def start_requests(self):
		# createCSV()
		json = {
			"source": [
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post",
				"New York Post"
			],
			"relatedStories": [
				"Hurricane Katrina",
				"Hussein Executed",
				"House Speaker",
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
				"https://nypost.com/2005/08/30/hurricane-katrina-spells-profit-for-oil-goons/",
				"https://nypost.com/2006/12/30/saddam-is-the-king-of-swing-bye-bye-to-butcher-of-baghdad-as-diabolical-dictator-is-hanged-before-dawn-to-delight-of-oppressed-iraqis/",
				"https://nypost.com/2007/01/13/pelosi-bill-blasted-as-pork-for-tuna/",
				"https://nypost.com/2008/11/05/barack-obama-wins-the-presidency/",
				"https://nypost.com/2009/10/14/swine-flu-prevention-kicks-into-high-gear-2/",
				"https://nypost.com/2010/05/12/gulf-of-mexico-massive-oil-spill/",
				"https://nypost.com/2011/03/12/9-0-earthquake-hits-japan/",
				"https://nypost.com/2012/08/13/london-olympics-closing-ceremony/",
				"https://nypost.com/2013/04/15/terror-attack-strikes-boston-marathon-more-than-130-injured-person-of-interest-idd/",
				"https://nypost.com/2014/03/15/russian-forces-move-into-ukraine-on-the-eve-of-referendum/",
				"https://nypost.com/2015/06/26/supreme-court-approves-gay-marriage-nationwide/",
				"https://nypost.com/2016/11/09/this-is-how-donald-trump-won-the-election/",
				"https://nypost.com/2017/01/22/trump-administration-disputes-crowd-numbers-at-inauguration/",
				"https://nypost.com/2018/07/09/brett-kavanaugh-is-an-excellent-pick-for-the-supreme-court/",
				"https://nypost.com/2019/09/22/military-apologizes-for-threatening-to-launch-stealth-bomber-at-storm-area-51-event/",
				"https://nypost.com/2020/05/28/everything-we-know-about-the-death-of-george-floyd/",
				"https://nypost.com/2021/01/07/dc-protests-how-a-mob-of-rioters-took-the-capitol-by-storm/"
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
