import cx_Oracle
import mybatis_mapper2sql
from day41sul.mylog import MyLog


class MyDaoStarget:
    def __init__(self):
        self.conn = cx_Oracle.connect('python/python@localhost:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_starget.xml')[0]
        
    def myselect(self,survey_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        MyLog().getLogger().debug(sql)
        rs = self.cs.execute(sql, (survey_id,))
        list = []
        for record in rs:
            list.append({'survey_id':record[0],'st_mobile':record[1],'complete_yn':record[2],'in_date':record[3],'in_user_id':record[4],'up_date':record[5],'up_user_id':record[6]})
        return list
    
    
    def myinsert(self,survey_id, st_mobile, complete_yn, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (survey_id, st_mobile, complete_yn, in_user_id, up_user_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

        
    def myupdate(self,survey_id, st_mobile, complete_yn, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")        
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (complete_yn, up_user_id, survey_id, st_mobile))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    
    def mydelete(self,survey_id, st_mobile):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")  
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (survey_id, st_mobile,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()
        
        
if __name__ == "__main__":
    dao = MyDaoStarget()

    
    
    