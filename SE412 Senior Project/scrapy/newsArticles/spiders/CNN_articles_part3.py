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
	name = "cnn3"

	def start_requests(self):
		# createCSV()
		json = {
			"source": [
				"CNN"
			],
			"relatedStories": [
				"Russia Invades Ukraine"
			],
			"urls": [
				"https://edition.cnn.com/2014/08/28/world/europe/ukraine-crisis/index.html"
			]
		}

		for i, url in enumerate(json["urls"]):
			yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(source=json["source"][i], relatedStory=json["relatedStories"][i]))



	def parse(self, response, source, relatedStory):
		data = []
		article = newspaper.Article(url = ' ')
		article.set_html(response.body)
		article.parse()

		cwd = os.getcwd()
		midpath = "newsArticles"
		save_path = "html"
		page = response.url.split("/")[-2]
		filename = f'ukraine-crisis.txt'
		completeName = os.path.join(cwd, midpath, save_path, filename)
		# write html to file
		# with open(completeName, 'wb') as f:
		# 	f.write(response.body)
		# self.log(f'Saved file {filename}')

		#read html to get title and test of article
		with open(completeName, 'rb') as fh:
			ht = fh.read()

		# print('TITLE: ', article.title)
		# print('TEXT: ', ht)
		# print(source)
		# print(relatedStory)
		data.append(source)
		data.append(relatedStory)
		data.append(article.title)
		data.append(ht)
		data.append(response.url)
		addToCSV(data)
