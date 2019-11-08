import sys
sys.path.append("..") # Adds higher directory to python modules path.

from selenium import webdriver
from ptt_spider.Search_ptt_index import Search_ptt_index 
from mysql_for_ptt.insert_msg import insert_msg

from mysql_for_ptt.insert_msg import insert_msg

driver = webdriver.Chrome("../chromedriver.exe")  
ptt_index = Search_ptt_index(driver)

page_list=ptt_index.get_page_list(34997)
msg_insert_to_db = insert_msg()


for page in page_list:
    
    print(page.nrec)
    print(page.title)
    print(page.url)
    print(page.author)
    
    
    data_MM = page.date.lstrip().split("/")[0]
    data_DD = page.date.lstrip().split("/")[1]
    sql_date_type="2019-"+data_MM+"-"+data_DD
    print(sql_date_type)
    
    page.set_up_url_index(34997)
    page.set_count_msg(50)
    
    msg_insert_to_db.create_article(int(page.nrec), page.title, page.author, page.url, sql_date_type,page.get_up_url_index(),page.get_count_msg())

    