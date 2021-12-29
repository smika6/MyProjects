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
# 	csvName = "articles5.csv"
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
	name = "wsj1"

	start_urls = ['https://sso.accounts.dowjones.com/login?state=hKFo2SBGVHhmbU83R1BFMXBoZkhQaE1qRFE2X1VnLUI0T3B6dqFupWxvZ2luo3RpZNkgbmZRWEVKOWZKbWlOd0k5Q1ZrdFVTODVNOU5NMU10ZjajY2lk2SA1aHNzRUFkTXkwbUpUSUNuSk52QzlUWEV3M1ZhN2pmTw&client=5hssEAdMy0mJTICnJNvC9TXEw3Va7jfO&protocol=oauth2&scope=openid%20idp_id%20roles%20email%20given_name%20family_name%20djid%20djUsername%20djStatus%20trackid%20tags%20prts%20suuid%20createTimestamp&response_type=code&redirect_uri=https%3A%2F%2Faccounts.wsj.com%2Fauth%2Fsso%2Flogin&nonce=9af37ba6-481c-4ae4-ab0a-db7aaebb927c&ui_locales=en-us-x-wsj-215-2&mars=-1&ns=prod%2Faccounts-wsj#!/signin-password']

	def parse(self, response):
		# print("##################################################")
		return scrapy.FormRequest.from_response(
			response,
			formdata={'username': 'carriveau.thomas@gmail.com', 'password': ' '},
			callback=self.after_login
		)

	def after_login(self, response):
		# print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print(response)
		print(response.status)
		# print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
		if(response.status == 200):
			# print("LOGIN PASSED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			# createCSV()
			json = {
				"source": [
					"The Wall Street Journal",
					"The Wall Street Journal",
					"The Wall Street Journal"
				],
				"relatedStories": [
					"Hurricane Katrina",
					"Hussein Executed",
					"House Speaker"
				],
				"urls": [
					"https://www.wsj.com/articles/SB122487570244867421",
					"https://www.wsj.com/articles/SB116738789247862458",
					"https://www.wsj.com/articles/SB116891896808477346"
				]
			}

			for i, url in enumerate(json["urls"]):
				print("GRAB SOME STUFF")
				headers = {
					'Connection': 'keep-alive',
					'Cache-Control': 'max-age=0',
					'DNT': '1',
					'Upgrade-Insecure-Requests': '1',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
					'Sec-Fetch-User': '?1',
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
					'Sec-Fetch-Site': 'same-origin',
					'Sec-Fetch-Mode': 'navigate',
					'Accept-Encoding': 'gzip, deflate, br',
					'Accept-Language': 'en-US,en;q=0.9',
				}

				yield scrapy.Request(url=url, callback=self.parse2, cb_kwargs=dict(source=json["source"][i], relatedStory=json["relatedStories"][i]), headers=headers)

	def parse2(self, response, source, relatedStory):
		print("MORE GRABBING STUFF")
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
