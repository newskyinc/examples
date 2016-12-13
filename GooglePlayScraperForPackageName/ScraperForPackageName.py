import urllib2
import urllib
from bs4 import BeautifulSoup



def searchMainURL(url):
	print url
	#html_content = urllib2.urlopen(url)
	html_content = open('googleSourceCode', 'r')
	soup = BeautifulSoup(html_content, "html.parser")

	file = open('apkNames2.txt', 'a')
	for two in soup.find_all("a", {"class": "see-more"}, {"id": "responsive-see-more"}):
		newURL = "https://play.google.com"
		newURL+=two.get("href", [])
		searchAllURL(newURL)

def searchAllURL(url):
	for one in soup.find_all("span", {"class": "preview-overlay-container"}):
	  file.write(one.get("data-docid", []))
	  file.write("\n")
	file.close()

	
URL = 'https://play.google.com/store/apps'
searchMainURL(URL)
	  


