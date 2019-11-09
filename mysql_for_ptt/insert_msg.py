import sys
sys.path.append("..") # Adds higher directory to python modules path.

from .db_operation import db_operation


class insert_msg():
    
    def __init__(self):
        self.db = db_operation()
    
    def create_article(self, nrec:int, title:str,author_name:str, url:str, post_date:str, up_url_index:int, count_msg:int):
        self.create_user(author_name)
        
        user_id = self.get_user_id(author_name)
        
        insert_article_sql = "insert into article (nrec, article_title, author_fk, article_url, post_time,up_url_index, count_msg) \
        Select %s,%s,%s,%s,%s,%s,%s Where not exists(select * from article where article_url=%s)"
        args = (nrec, title, user_id, url, post_date, up_url_index, count_msg, url)
        
        self.db.execute(insert_article_sql, args)
  
    def create_user(self,user_name:str):
        inster_user_sql = "insert into test_user (user_name)\
                           Select %s Where not exists \
                           (select * from test_user where user_name=%s)" 
        args = (user_name,user_name)             
        self.db.execute(inster_user_sql, args)
       
    def create_msg(self, msg:str, msg_push_tab:str, msg_time:str, user_name:str, article_url:str,ipv4:str):   
        
        self.create_user(user_name)
        user_id = self.get_user_id(user_name)
        
        article_url_id = self.get_article_id(article_url)
        
        inster_msg_sql = "INSERT INTO msg_2(msg,msg_push_tab,msg_time,user_id_fk,article_id_fk,ipv4) \
                        VALUES (%s,%s,%s,%s,%s,%s)"
        args = (msg, msg_push_tab, msg_time, user_id, article_url_id, ipv4)
        
        self.db.execute(inster_msg_sql, args)
        

    def get_user_id(self,user_name:str)->int:
        SELECT_SQL ="SELECT id from test_user WHERE user_name = %s "
        
        self.db.execute(SELECT_SQL,(user_name,) )
        user_id = self.db.fetchone()[0]
        return user_id
    
    def get_article_id(self,url:str)->int:
        SELECT_SQL ="SELECT id from article WHERE article_url = %s "
        self.db.execute( SELECT_SQL, (url,) )
        article_id = self.db.fetchone()[0]
        return article_id
        
    def close(self):
        self.db.colse()
    




