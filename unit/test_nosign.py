import sys
sys.path.append("..") # Adds higher directory to python modules path.

from selenium import webdriver
from ptt_spider.Search_ptt_index import Search_ptt_index
from ptt_spider.Analysis_page_msg import Analysis_page_msg



driver = webdriver.Chrome("../chromedriver.exe")  
ptt_index = Search_ptt_index(driver)
analysis_page = Analysis_page_msg(driver)

ptt_index.driver_goto_ptt_url("https://www.ptt.cc/bbs/Gossiping/M.1572699456.A.85F.html")
source_html = ptt_index.get_source_html()
analysis_page.msg_detail_info(source_html)

while(analysis_page.have_next()):
    msg_list = analysis_page.get_next_msg()
    print(msg_list)







