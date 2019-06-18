# -*- coding: utf-8 -*-
# Copyright Ramón Vila Ferreres 2019
# github.com/rmon-vfer/

from zipfile import ZipFile
import requests
import cfscrape
import json
import shutil
import os

scraper = cfscrape.create_scraper() # Bypass CloudFlare protection

def urlToImage(url, filename):
	downloadFile(url, filename)
	extractImage(filename)

	for file in os.listdir():
		if file.endswith("mwa"):
			shutil.remove(file)

def extractImage(filename):
	print("Extracting file...")
	print(filename)
	with ZipFile(filename, "r") as z:
	    with open('image', 'wb') as f:
	        f.write(z.read("image"))

	shutil.move("image", "./extracted/" + filename)

def downloadFile(fileUrl, filename):
	print("Downloading file...")

	r = requests.get(fileUrl)
	open(filename, 'wb').write(r.content)

def getWallpaperList():

	url = "https://api.mangarockhd.com/parse/functions/getWallpaperList"
	data = json.dumps({
		"experiment" :"default", 
		"variant"    :"default", 
		"start"      : 0, 
		"end"        : 1, 
		"isNew"      : True})

	headers = {
		"Host"                   :  "api.mangarockhd.com", 
		"x-parse-application-id" :  "DOTecsAUU0hHsVe50hQqCltNmpzx5hbwJB60FfyM", 
		"x-parse-client-key"     :  "lpY0gkLg4LOtrTAtNT1L1vwC1llTWkr0F8wusC5i", 
		"accept-encoding"        :  "gzip", 
		"user-agent"             :  "okhttp/3.9.1"
	}

	response = scraper.post(url, data=data, headers=headers)
	response_data = response.content

	response_data = json.loads(response_data.decode("utf-8"))
	return json.dumps(response_data, indent=4, sort_keys=True)


def main():
	print("Obtaining Wallpaper List from MangaRock servers...")
	data = getWallpaperList()
	with open('wallpaper_data.json', 'w') as fp:
		fp.write(data)

	data = json.loads(data)
	item = data["result"]["items"][1]
	urlToImage(item["fileUrl"], item["objectId"])

	#print(json.dumps(data["result"]["items"][1], indent=4, sort_keys=True))

	print("Succesfully saved wallpaper data from mangarock servers!")

main()
