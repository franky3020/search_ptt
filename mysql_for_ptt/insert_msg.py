import sys
sys.path.append("..") # Adds higher directory to python modules path.

from .db_operation import db_operation


class insert_msg():
    
    def __init__(self):
        self.db = db_operation()
    
    def create_article(self, nrec:str, title:str,author_name:str, url:str, post_date:str, up_url_index:int, count_msg:int):
        self.create_user(author_name)
        
        user_id = self.get_user_id(author_name)[0]
        print("debug: ",user_id)
        
        insert_article_sql = "insert into article (nrec, article_title, author_fk, article_url, post_time,up_url_index, count_msg) \
        Select {},'{}',{},'{}','{}',{},{} Where not exists(select * from article where article_url='{}')"
        
        self.db.execute(insert_article_sql.format(nrec, title, user_id, url, post_date, up_url_index, count_msg, url))
  
    def create_user(self,user_name:str):
        inster_user_sql = "insert into test_user (user_name)\
                           Select '{}' Where not exists \
                           (select * from test_user where user_name='{}')" 
                           
        self.db.execute(inster_user_sql.format(user_name,user_name))
       
    def get_user_id(self,user_name:str)->int:
        SELECT_SQL ="SELECT id from test_user WHERE user_name = '{}' "
        self.db.execute(SELECT_SQL.format(user_name))
        return self.db.fetchone()
    
    def get_article_id(self,url:str)->int:
        SELECT_SQL ="SELECT id from article WHERE article_url = '{}' "
        self.db.execute( SELECT_SQL.format(url) )
        return self.db.fetchone()
        
    def create_msg(self):   
        pass 
    
    def close(self):
        self.db.colse()
    




