from TH_functions import *


DayUrls = TH_DayUrl_Generator()

for i in DayUrls:
	print i 


urls = 'http://www.thehindu.com/todays-paper/tp-opinion/the-only-way-to-deal-with-the-chinese-is-directly/article19260841.ece'
all_info = TH_Article_Content_Extractor(urls)


for i in all_info:
	 print i+" ----- " +all_info[i]