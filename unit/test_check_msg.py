import sys
sys.path.append("..") # Adds higher directory to python modules path.
from mysql_for_ptt.Check_msg import Check_msg


check_msg = Check_msg()
print(check_msg.exist_user("frrr"))
print(check_msg.exist_user("frrr1111"))
print(check_msg.exist_article_id("https://www.ptt.cc/bbs/Gossiping/M.1571805062.A.071.html"))
