from selenium import webdriver
from Search_ptt_index import Search_ptt_index
from Analysis_page_msg import Analysis_page_msg

driver = webdriver.Chrome("./chromedriver.exe")  
ptt_index = Search_ptt_index(driver)
analysis_page = Analysis_page_msg(driver)

page_list = ptt_index.get_page_list(31000)
print(page_list)



for page in page_list:

    print(page.get_title())
    driver.get( page.get_url() )
    
    source_html = driver.page_source
    analysis_page.msg_detail_info(source_html)

    while(analysis_page.have_next()):
        msg_list = analysis_page.get_next_msg()
        print(msg_list)
        
  
 
# sql = "INSERT INTO ptt_users_v2 (user_name, msg, msg_push_tab, msg_time, article_title, article_url \
# )VALUES (%s, %s, %s, %s, %s, %s)"

# val = (user, msg, evaluation, self.re_datetime_sql(push_time), now_page_title, now_page_url)
# self.db.execute(sql,val)

          




        
        
    


 