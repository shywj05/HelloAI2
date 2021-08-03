import cx_Oracle
import mybatis_mapper2sql
from day41sul.mylog import MyLog

class MyDaoSnotice:
    def __init__(self):
        self.conn = cx_Oracle.connect('python/python@localhost:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_snotice.xml')[0]
        
    def myselect_list(self,user_id,search):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list")
        MyLog().getLogger().debug(sql)
        rs = self.cs.execute(sql,(user_id,search,) )
        list = []
        for record in rs:
            list.append({'b_seq':record[0],'display_yn':record[1],'title':record[2],'content':record[3],'attach_path':record[4],'attach_file':record[5], 'hit':record[6], 'in_date':record[7],'in_user_id':record[8],'up_date':record[9],'up_user_id':record[10],'in_user_name':record[11]})
        return list
    
    def myselect(self,b_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        MyLog().getLogger().debug(sql)
        rs = self.cs.execute(sql, (b_seq,) )
        obj = None
        for record in rs:
            obj = {'b_seq':record[0],'display_yn':record[1],'title':record[2],'content':record[3],'attach_path':record[4],'attach_file':record[5], 'hit':record[6], 'in_date':record[7],'in_user_id':record[8],'up_date':record[9],'up_user_id':record[10],'in_user_name':record[11]}
        return obj
    
    
    def myinsert(self,b_seq, display_yn, title, content, attach_path, attach_file, hit, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (display_yn, title, content, attach_path, attach_file, in_user_id, up_user_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

        
    def myupdate(self,b_seq, display_yn, title, content, attach_path, attach_file, hit, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")        
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (display_yn, title, content, attach_path, attach_file, up_user_id, b_seq))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def mydel_img(self,b_seq,user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "del_img")  
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (user_id,b_seq))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def myhit(self,b_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "hit")  
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (b_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def mydelete(self,b_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")  
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (b_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()
        
        
if __name__ == "__main__":
    dao = MyDaoSnotice()
    obj = dao.myselect('1')
    print(obj)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    