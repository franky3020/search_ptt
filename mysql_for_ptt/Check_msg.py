import sys
sys.path.append("..") # Adds higher directory to python modules path.

from .db_operation import db_operation


class Check_msg():
    
    def __init__(self):
        self.db = db_operation()
        
    def exist_article_id(self, url:str) -> bool:
        SELECT_SQL ="SELECT id from article WHERE article_url = %s "
        self.db.execute( SELECT_SQL, (url,) )
        fetchone_res = self.db.fetchone()
        if(fetchone_res != None):
            return True
        else:
            return False
    
    def exist_user(self, user_name:str) -> bool:
        SELECT_SQL ="SELECT id from test_user WHERE user_name = %s "
        
        self.db.execute(SELECT_SQL,(user_name,) )
        fetchone_res = self.db.fetchone()
        if(fetchone_res != None):
            return True
        else:
            return False
    
    def isNeedUpdata(self):
        pass
            
        
    def close(self):
        self.db.colse()
    