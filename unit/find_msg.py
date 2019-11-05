import sys
sys.path.append("..") # Adds higher directory to python modules path.
from selenium import webdriver
from ptt_spider.Search_ptt_index import Search_ptt_index
from ptt_spider.Analysis_page_msg import Analysis_page_msg

driver = webdriver.Chrome("../chromedriver.exe")  
ptt_index = Search_ptt_index(driver)

ptt_index.driver_goto_ptt_url("https://www.ptt.cc/bbs/Gossiping/index34997.html")
soup_list = ptt_index.find_each_article(ptt_index.get_source_html())

page_msg = Analysis_page_msg(driver)

page_msg.driver_goto_ptt_url(ptt_index.find_article_url(soup_list[0]))
    

article_meta_soup = page_msg.find_article_metaline(page_msg.get_source_html())
page_msg.find_msg(article_meta_soup)
    