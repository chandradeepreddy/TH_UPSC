from bs4 import BeautifulSoup
import urllib2
import re

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

def Hindu_Article_Extractor(URL):
	""" 
	This function takes in a hindu article url and 
	returns a dictionary with following details:
	Title
	Caption
	Body
	Image URL
	Author
	Date time
	"""
	try:
		title =BeautifulSoup(urllib2.urlopen(URL)).find_all("h1",{"class":re.compile("title")})[0].text.strip().encode('utf-8')
	except IndexError:
		title = ''

	try:
		caption =BeautifulSoup(urllib2.urlopen(URL)).find_all("h2",{"class":re.compile("intro")})[0].text.strip().encode('utf-8')
	except IndexError:
		caption = ''

	try:
		body =BeautifulSoup(urllib2.urlopen(URL)).find_all("div",{"id":re.compile("content-body-*")})[0].text.strip().encode('utf-8')
	except IndexError:
		body = ''

	try:
		imgUrl =re.sub('FREE_215','FREE_660',BeautifulSoup(urllib2.urlopen(URL)).find_all("img",{"class":re.compile("media-object adaptive placeholder lead-img")})[0]['data-proxy-image'])
	except IndexError:
		imgUrl = ''

	try:
		author = BeautifulSoup(urllib2.urlopen(URL)).find_all("a",{"class":re.compile("auth-nm lnk|auth-nm no-lnk")})[0].text.strip().encode('utf-8')
	except IndexError:
		author = ''

	try:
		tmstmp = BeautifulSoup(urllib2.urlopen(URL)).find_all("div",{"class":re.compile("ut-container")})[0].text.strip().encode('utf-8')
	except IndexError:
		tmstmp = ''

	
	row = {}
	row["Title"] = title
	row["Caption"] = caption
	row["Body"] = body
	row["ImgUrl"] = imgUrl
	row["Author"] = author
	row["DateTime"] = tmstmp
	return row






####Comments
#Used below commands on console to fix python encoding issue
#set PYTHONIOENCODING=UTF-8
#pip --version
