import sys
sys.path.append("..") # Adds higher directory to python modules path.
from selenium import webdriver
from ptt_spider.Search_ptt_index import Search_ptt_index
from ptt_spider.Analysis_page_msg import Analysis_page_msg

driver = webdriver.Chrome("../chromedriver.exe")  
ptt_page_driver = Search_ptt_index(driver)
page_msg_driver = Analysis_page_msg(driver)

page_list = ptt_page_driver.get_page_list(39000)
for page in page_list:
    msg_soup_list = page_msg_driver.get_msg_soup_list(page.url)
    print(page.title)
    for msg in msg_soup_list:
        msg.msg



    
    