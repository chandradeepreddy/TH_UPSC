from TH_functions import *

urls = 'http://www.thehindu.com/todays-paper/tp-opinion/the-only-way-to-deal-with-the-chinese-is-directly/article19260841.ece'
all_info = Hindu_Article_Extractor(urls)


for i in all_info:
	 print i+" ----- " +all_info[i]