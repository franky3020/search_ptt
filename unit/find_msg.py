import sys
sys.path.append("..") # Adds higher directory to python modules path.
from selenium import webdriver
from ptt_spider.Search_ptt_index import Search_ptt_index
from ptt_spider.Analysis_page_msg import Analysis_page_msg

driver = webdriver.Chrome("../chromedriver.exe")  

page_msg = Analysis_page_msg(driver)
msg_soup_list = page_msg.get_msg_soup_list("https://www.ptt.cc/bbs/Gossiping/M.1572918440.A.543.html")


for msg in msg_soup_list:
    print(msg.msg)
    
    