from selenium import webdriver
from ptt_spider.Search_ptt_index import Search_ptt_index
from ptt_spider.Analysis_page_msg import Analysis_page_msg
from mysql_for_ptt.insert_msg import insert_msg

driver = webdriver.Chrome("./chromedriver.exe")  
ptt_index_page = Search_ptt_index(driver)
ptt_msgBoard_page = Analysis_page_msg(driver)

ptt_insert_to_db = insert_msg()

for page_index in range(38000,39000):
   
    page_list = ptt_index_page.get_page_list(page_index)
    
    for page in page_list:
        page.set_up_url_index(page_index)#
        msgObject_list = ptt_msgBoard_page.get_msgObject_list(page.url)
        
        is_insert_page_to_db = False
        for msg in msgObject_list:
            
            if is_insert_page_to_db is False:#first time run is need insert author and article to db
                page.set_count_msg(len(msgObject_list))
                ptt_insert_to_db.create_article(int(page.nrec), page.title, page.author, page.url, page.get_sql_date_type(),page.get_up_url_index(),page.get_count_msg())
                
                is_insert_page_to_db = True
                
            try:
                ptt_insert_to_db.create_msg(msg.msg, msg.evaluation, msg.datetime, msg.user, page.url, msg.ip)
            except:
                print("[ERROR] page_index: ",page_index,", ",page.title,", ",msg.msg,", ", sys.exc_info()[0])
                
    
    print(page_index,"is ok!!")
    


          




        
        
    


 