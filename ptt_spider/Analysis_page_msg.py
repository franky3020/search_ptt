from bs4 import BeautifulSoup
import re
from .ptt_page import ptt_page
import time

class Analysis_page_msg():
    def __init__(self,driver):
        self.driver = driver 
        self.msg_list = []
        self.current_index = 0
        self.source_html = None
        
        
    def msg_detail_info(self,source_code):
        
        source_code = self.driver.page_source
        soup = BeautifulSoup(source_code, "html.parser")
    
        push_box = soup.find_all("div", attrs={"class": "push"})
        for push in push_box:
            user_dict={}
            
            user_dict['evaluation'] = push.find("span", attrs={"class": "push-tag"}).text
            user_dict['user']  = push.find("span", attrs={"class": "push-userid"}).text
            user_dict['msg'] = push.find("span", attrs={"class": "push-content"}).text
            
            push_ip = push.find("span", attrs={"class": "push-ipdatetime"}).text
            user_dict['ip'] = self.re_ip(push_ip)
            
            push_time = push.find("span", attrs={"class": "push-ipdatetime"}).text
            user_dict['datetime'] = self.re_datetime_sql(push_time)
            
            self.msg_list.append(user_dict)
            
            
    def find_article_metaline(self,source_code:str)->object:
        soup = BeautifulSoup(source_code, "html.parser")
        meta_article_soup = soup.find("div", attrs={"id": "main-content"})
        return meta_article_soup
        
    def find_msg(self,meta_article_soup):
        print(meta_article_soup)
        push_mag = meta_article_soup.find("span")
        print(push_mag.text)
    
    
            
    def get_next_msg(self) -> dict:
        user_msg_dict = self.msg_list[self.current_index]
        self.current_index = self.current_index + 1 
        return user_msg_dict
    
    def have_next(self):
        if( len(self.msg_list) == self.current_index):
            return False
        else:
            return True
            
    def re_ip(self, in_str)->str:  #解析IP
        pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
        date_str = re.search(pattern,in_str)
        if date_str:
            return date_str.group(0)  
        else:
            return None
    
    def re_datetime_sql(self, push_time) -> str:
        datetime = "2019-"
        pattern = r"[0-9]{1,2}/[0-9]{1,2}"
        re_date = re.search(pattern,push_time)
        
        if(re_date):
            date_str = re_date.group(0)
            datetime = datetime + date_str.split("/")[0] + "-" + date_str.split("/")[1] + " "
        else:
            return None
        
        
        pattern = r"[0-9]{1,2}:[0-9]{1,2}"
        re_time = re.search(pattern,push_time)
        
        if(re_time):
            time_str = re_time.group(0)
            datatime = datetime + time_str.split(":")[0] + ":" + time_str.split(":")[1] + ":00"
        else:
            return None
        
        
        return datatime
        
        
    def driver_goto_ptt_url(self,url):
        self.driver.get(url)
        if(self.driver.current_url != url):#被導到檢查介面
            time.sleep(4)
            self.driver.find_element_by_name("yes").click()#按檢查介面的yes
        self.source_html = self.driver.page_source
        
        
    def get_source_html(self):
        
        if(self.source_html != None):
            return self.source_html
        else:
            raise Exception("not hava source_html ")