from bs4 import BeautifulSoup
import re
from .ptt_page import ptt_page
from .ptt_msg import ptt_msg
import time
from bs4 import Tag, NavigableString, BeautifulSoup
import copy

class Analysis_page_msg():
    def __init__(self,driver):
        self.driver = driver 
        self.source_html = None
        self.msg_soup_list = []
        
    def get_msgObject_list(self,url:str)->list:
        self.driver_goto_ptt_url(url)
        article_meta_soup = self.find_article_metaline(self.source_html)
        self.find_msg(article_meta_soup)
        return self.msg_soup_list
    
    def find_article_metaline(self,source_code:str)->object:
        soup = BeautifulSoup(source_code, "html.parser")
        meta_article_soup = soup.find("div", attrs={"id": "main-content"})
        return meta_article_soup
        
    def find_msg(self,meta_article_soup):
        push_mag = meta_article_soup.find("span",attrs={"class": "f2"},text = re.compile("※ 發信站:.*"))
       
        first_push_soup=None
        current_soup = push_mag.nextSibling
        if(current_soup == None):
            return
            
        while(True):
            if(isinstance (current_soup, Tag) and current_soup.has_attr("class") and current_soup.attrs['class'] == ['push']):
                first_push_soup = current_soup
                break
            current_soup = current_soup.nextSibling
            if(current_soup == None):
                return
               
        current_soup =  first_push_soup
        
        while(True):
            if(isinstance (current_soup, Tag) and current_soup.has_attr("class") and current_soup.attrs['class'] == ['push']):
                self.msg_soup_list.append(self.take_out_info_from_msg(current_soup))
                
            current_soup = current_soup.nextSibling
            if(current_soup == None):
                return
    
    def take_out_info_from_msg(self, msg_soup) -> object:
        user_dict={}
            
        user_dict['evaluation'] = msg_soup.find("span", attrs={"class": "push-tag"}).text
        user_dict['user']  = msg_soup.find("span", attrs={"class": "push-userid"}).text
        user_dict['msg'] = msg_soup.find("span", attrs={"class": "push-content"}).text
        
        push_ip = msg_soup.find("span", attrs={"class": "push-ipdatetime"}).text
        user_dict['ip'] = self.re_ip(push_ip)
        
        push_time = msg_soup.find("span", attrs={"class": "push-ipdatetime"}).text
        user_dict['datetime'] = self.re_datetime_sql(push_time)
        
        
        ptt_msg_tmp = ptt_msg(user_dict['evaluation'], user_dict['user'], user_dict['msg'], user_dict['ip'], user_dict['datetime'])
        return ptt_msg_tmp
        
    
    def msg_soup_find_msg_push(self, index:int) -> dict:
        if(index>=0):
            return self.msg_soup_list[index]
        else:
            raise IndexError 

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
        
    def msg_push_count(self)->int:
        return len(self.msg_soup_list)
        
    def get_source_html(self):
        
        if(self.source_html != None):
            return self.source_html
        else:
            raise Exception("not hava source_html ")