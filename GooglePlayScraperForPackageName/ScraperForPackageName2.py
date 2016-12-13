import urllib2
import urllib
from bs4 import BeautifulSoup

def findCatagoryNames():
	list_content = open('catagoryNames.txt', 'r')
	soup1 = BeautifulSoup(list_content, "html.parser")
	for two in soup1.find_all("a", {"class": "child-submenu-link"}):
		newURL = "https://play.google.com"
		newURL+=two.get("href", [])
		searchMainURL(newURL)

def searchMainURL(url):
	print url
	#html_content = urllib2.urlopen(url)
	html_content = open('googleSource2.txt', 'r')
	soup2 = BeautifulSoup(html_content, "html.parser")

	for two in soup2.find_all("a", {"class": "see-more"}, {"id": "responsive-see-more"}):
		newURL = "https://play.google.com"
		newURL+=two.get("href", [])
		searchAllURL(newURL)

def searchAllURL(url):
	html_content = urllib2.urlopen(url)
	soup3 = BeautifulSoup(html_content, "html.parser")
	file = open('apkNames2.txt', 'a')
	for one in soup3.find_all("span", {"class": "preview-overlay-container"}):
	  file.write(one.get("data-docid", []))
	  file.write("\n")
	file.close()


findCatagoryNames()
URL = 'https://play.google.com/store/apps'
searchMainURL(URL)
	  


