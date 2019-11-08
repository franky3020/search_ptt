import sys
sys.path.append("..") # Adds higher directory to python modules path.

from selenium import webdriver
# from ptt_spider.Search_ptt_index import Search_ptt_index
from ptt_spider.Search_ptt_index import Search_ptt_index 

driver = webdriver.Chrome("../chromedriver.exe")  
ptt_index = Search_ptt_index(driver)

page_list=ptt_index.get_page_list(34997)

for page in page_list:
    
    
    
    print(page.nrec)
    print(page.url)
    print(page.title)
    print(page.author)
    print(page.date)
    
    
    
    


