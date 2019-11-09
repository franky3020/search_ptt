class ptt_page():
    def __init__(self, nrec:int, title:str, url:str, author:str, date:str):
        self.nrec = nrec
        self.url = url
        self.title = title
        self.author = author
        self.date = date
        
        self.up_url_index = None
        self.count_msg = None
    
    def set_up_url_index(self,index:int):
        self.up_url_index = int(index)
        
    def set_count_msg(self,count:int):
        self.count_msg = int(count)
        
    def get_up_url_index(self):
        if(self.up_url_index != None):
            return self.up_url_index
        else:
            raise Exception("not hava up_url_index ")
        
    def get_count_msg(self):
        if(self.count_msg != None):
            return self.count_msg
        else:
            raise Exception("not hava count_msg")
    
    def get_sql_date_type(self):
        data_MM = self.date.lstrip().split("/")[0]
        data_DD = self.date.lstrip().split("/")[1]
        sql_date_type="2019-"+data_MM+"-"+data_DD
        return sql_date_type
        
        
 