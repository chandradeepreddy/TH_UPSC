from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import urllib2
import re
from datetime import date, timedelta
import warnings
import collections


warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

def TH_Article_Content_Extractor(ArtURL):
	""" 
	This function takes in a hindu article url and 
	returns a dictionary with following details:
	Title
	Caption
	Body
	Image URL
	Author
	Date time.
	returns a dictionary
	"""
	try:
		title =BeautifulSoup(urllib2.urlopen(ArtURL)).find_all("h1",{"class":re.compile("title")})[0].text.strip().encode('utf-8')
	except IndexError:
		title = ''

	try:
		caption =BeautifulSoup(urllib2.urlopen(ArtURL)).find_all("h2",{"class":re.compile("intro")})[0].text.strip().encode('utf-8')
	except IndexError:
		caption = ''

	try:
		body =BeautifulSoup(urllib2.urlopen(ArtURL)).find_all("div",{"id":re.compile("content-body-*")})[0].text.strip().encode('utf-8')
	except IndexError:
		body = ''

	try:
		imgUrl =re.sub('FREE_215','FREE_660',BeautifulSoup(urllib2.urlopen(ArtURL)).find_all("img",{"class":re.compile("media-object adaptive placeholder lead-img")})[0]['data-proxy-image'])
	except IndexError:
		imgUrl = ''

	try:
		author = BeautifulSoup(urllib2.urlopen(ArtURL)).find_all("a",{"class":re.compile("auth-nm lnk|auth-nm no-lnk")})[0].text.strip().encode('utf-8')
	except IndexError:
		author = ''

	try:
		tmstmp = BeautifulSoup(urllib2.urlopen(ArtURL)).find_all("div",{"class":re.compile("ut-container")})[0].text.strip().encode('utf-8')
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

def TH_DayUrl_Generator():
	""" 
	This function takes in a date range and 
	give a list of hindu daily urls from 
	the hindu archives page ( print edition).
	returns a list
	"""
	print "Enter Start and End Date details"
	start_year = int(raw_input("Enter the start date year: "))
	start_month = int(raw_input("Enter the start date month: "))
	start_day = int(raw_input("Enter the start date day: "))
	end_year = int(raw_input("Enter the end date year: "))
	end_month = int(raw_input("Enter the end date month: "))
	end_day = int(raw_input("Enter the end date day: "))

	DayUrls =[]
	Start_Date = date(start_year, start_month, start_day)  # start date
	End_Date = date(end_year, end_month, end_day)  # end date
	delta = (End_Date-Start_Date)

	for i in range(delta.days + 1):
		DayUrls.append('http://www.thehindu.com/archive/print/'+str((Start_Date + timedelta(days=i)).year)+'/'+str((Start_Date + timedelta(days=i)).strftime('%m'))+'/'+str((Start_Date + timedelta(days=i)).strftime('%d'))+'/')
	return DayUrls



def TH_Article_URL__Extractor(DayUrls_list):
	""" 
	This function takes in a daily hindu url list
	and gives all artilce links from that day along with 
	the date. returns a list
	"""
	ArtUrls = {}
	for i in range(len(DayUrls_list)):
		soup = BeautifulSoup(urllib2.urlopen(DayUrls_list[i]))
		soup.prettify()
		AllUrls = soup.findAll('a', href=True)
		Articles = [AllUrls[url]['href'] for url in range(len(AllUrls)) if '.ece' in AllUrls[url]['href'] and '/todays-paper/' in AllUrls[url]['href'] ]
		
		for j in range(len(Articles)):
			print str(re.sub('[^0-9]','',DayUrls_list[i])) +' '+Articles[j]
			ArtUrls[Articles[j].encode('utf-8')] = str(re.sub('[^0-9]','',DayUrls_list[i]))
	
	return ArtUrls


####Comments
#Used below commands on console to fix python encoding issue
#set PYTHONIOENCODING=UTF-8
#pip --version
