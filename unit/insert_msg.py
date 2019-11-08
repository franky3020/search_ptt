import sys
sys.path.append("..") # Adds higher directory to python modules path.
from selenium import webdriver
from ptt_spider.Search_ptt_index import Search_ptt_index
from ptt_spider.Analysis_page_msg import Analysis_page_msg
from mysql_for_ptt.insert_msg import insert_msg

driver = webdriver.Chrome("../chromedriver.exe")  

page_msg = Analysis_page_msg(driver)
search_html_url = 'https://www.ptt.cc/bbs/Gossiping/M.1568869608.A.E36.html'
msg_soup_list = page_msg.get_msgObject_list(search_html_url)

mag_insert_to_db = insert_msg()

# self.evaluation = evaluation
# self.user = user
# self.msg = msg
# self.ip = ip
# self.datetime = datetime


for msg in msg_soup_list:
    print(msg.evaluation)
    print(msg.user)
    print(msg.msg)
    print(msg.ip)
    print(msg.datetime)

    mag_insert_to_db.create_msg(msg.msg, msg.evaluation, msg.datetime, msg.user, search_html_url, msg.ip)