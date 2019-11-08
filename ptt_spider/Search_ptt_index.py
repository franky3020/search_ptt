from bs4 import BeautifulSoup
import re
import time
from .ptt_page import ptt_page

class Search_ptt_index():
    def __init__(self,driver):
        self.driver = driver 
        self.source_html = None
        
    def get_page_list(self,index:int)-> list: 
        page_list =[]
        self.driver_goto_ptt_url( "https://www.ptt.cc/bbs/Gossiping/index"+str(index)+".html" )
        article_soup=self.find_each_article(self.get_source_html())
        
        for soup in article_soup:
            try:
                nrec = self.find_nrec(soup)
                title = self.find_title(soup)
                article_url = self.find_article_url(soup)
                author = self.find_author(soup)
                
                post_data = self.find_post_data(soup)
                
                ptt_page_tmp = ptt_page(nrec, title, article_url, author, post_data)
            
                page_list.append(ptt_page_tmp)
            except:
                print("soup error in search: ", index)
                pass
            
            
        return page_list.copy()
    
    def find_each_article(self, source:str) -> list:
        soup = BeautifulSoup(self.source_html, "html.parser")
        try:
            every_page=soup.find_all("div", attrs={"class": "r-ent"})
        except:
            print("error in find_each_article")
            every_page = []
        
        return every_page
            
    
    def find_nrec(self,soupPage:object)->int:
        try:
            n_rec = soupPage.find("div", attrs={"class": "nrec"}).find('span').text
            n_rec = int(n_rec)
        except:
            n_rec = 0
        return n_rec
      
        
    def find_title(self,soupPage:object)->str:
        return soupPage.find("div", attrs={"class": "title"}).find('a').text 
            
    def find_article_url(self,soupPage:object)->str:
        a_url=soupPage.find("div", attrs={"class": "title"}).find('a')['href']
        return "https://www.ptt.cc"+a_url
    
    def find_author(self,soupPage:object)->str:
        try:
            author_name = soupPage.find("div", attrs={"class": "meta"}).find("div", attrs={"class": "author"}).text
        except:
            author_name = None
            
        return author_name
        
    def find_post_data(self,soupPage:object)->str:
        try:
            post_data = soupPage.find("div", attrs={"class": "meta"}).find("div", attrs={"class": "date"}).text
        except:
            post_data = None
            
        return post_data
            
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
        
        
        
    
    
    
    