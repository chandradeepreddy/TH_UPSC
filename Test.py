from TH_functions import *

urls = 'http://www.thehindu.com/todays-paper/tp-national/india-slips-in-human-development-index/article17567402.ece'
all_info = Hindu_URL_Extractor(urls)


for i in all_info:
	 print i+" ----- " +all_info[i]