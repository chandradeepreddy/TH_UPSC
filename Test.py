from TH_functions import *


DayUrls = TH_DayUrl_Generator()

articl_dict = TH_Article_URL__Extractor(DayUrls)

for i in  articl_dict:
	for j in  TH_Article_Content_Extractor(i):
		print j + '------'+TH_Article_Content_Extractor(i)[j]


# for i in all_info:
# 	 print i+" ----- " +all_info[i]