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



def createCSV():
	header = ['Source Name', 'Related Story', 'Title', 'Text', 'URL']
	cwd = os.getcwd()
	csvName = "articles.csv"
	midpath = "newsArticles"
	csv_path = "csv"
	csvFile = os.path.join(cwd, midpath, csv_path, csvName)

	with open(csvFile, 'w', encoding='UTF8', newline='') as f:
		writer = csv.writer(f)

		# write the header
		writer.writerow(header)



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
	name = "cnn1"

	def start_requests(self):
		createCSV()
		json = {
			"source": [
				"CNN",
				"CNN",
				"CNN",
				"CNN",
				"CNN",
				"CNN",
				"CNN",
				"CNN",
				"CNN",
				"CNN",
				"CNN",
				"CNN",
				"CNN",
				"CNN",
				"CNN",
				"CNN",
				"CNN"
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
				"Gay Marriage ",
				"Trump Elected",
				"Trump Inauguration",
				"Brett Kavanaugh picked for SCJ",
				"Area 51 Raid",
				"January 6th"

			],
			"urls": [
				"https://www.cnn.com/2005/WEATHER/08/28/hurricane.katrina/",
				"https://www.cnn.com/2006/WORLD/meast/12/29/hussein/",
				"http://edition.cnn.com/2007/POLITICS/01/04/pelosi.transcript/index.html",
				"http://edition.cnn.com/2008/POLITICS/11/04/election.president/index.html",
				"http://www.cnn.com/2009/HEALTH/11/12/h1n1.flu.deaths/index.html",
				"http://www.cnn.com/2010/US/05/01/louisiana.oil.spill/index.html",
				"http://www.cnn.com/2011/WORLD/asiapcf/03/11/japan.quake/index.html",
				"https://www.cnn.com/2012/08/12/sport/london-olympics-close-quest/index.html",
				"https://www.cnn.com/2013/04/15/us/boston-marathon-explosions/index.html",
				"https://www.cnn.com/2015/06/26/politics/supreme-court-same-sex-marriage-ruling/index.html",
				"https://www.cnn.com/2016/12/21/politics/donald-trump-hillary-clinton-popular-vote-final-count/index.html",
				"https://www.cnn.com/2017/01/20/politics/donald-trump-inauguration-highlights/index.html",
				"https://www.cnn.com/2018/07/09/politics/trump-supreme-court-pick/index.html",
				"https://www.cnn.com/travel/article/area-51-raid-weekend-event-trnd/index.html",
				"https://www.cnn.com/2021/01/07/us/five-things-january-7-trnd/index.html"
			]
		}

		for i, url in enumerate(json["urls"]):
			yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(source=json["source"][i], relatedStory=json["relatedStories"][i]))



	def parse(self, response, source, relatedStory):
		data = []
		article = newspaper.Article(url = ' ')
		article.set_html(response.body)
		article.parse()

		# cwd = os.getcwd()
		# midpath = "newsArticles"
		# save_path = "html"
		# page = response.url.split("/")[-2]
		# filename = f'quotes-{page}.html'
		# completeName = os.path.join(cwd, midpath, save_path, filename)
		# # write html to file
		# with open(completeName, 'wb') as f:
		# 	f.write(response.body)
		# self.log(f'Saved file {filename}')

		# print('TITLE: ', article.title)
		# print(source)
		# print(relatedStory)
		data.append(source)
		data.append(relatedStory)
		data.append(article.title)
		data.append(article.text)
		data.append(response.url)
		addToCSV(data)
