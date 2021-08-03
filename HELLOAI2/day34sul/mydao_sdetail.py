import cx_Oracle
import mybatis_mapper2sql
from day34sul.mylog import MyLog


class MyDaoSdetail:
    def __init__(self):
        self.conn = cx_Oracle.connect('python/python@localhost:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_sdetail.xml')[0]
        
    def myselect(self, survey_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        MyLog().getLogger().debug(sql)
        rs = self.cs.execute(sql, (survey_id,))
        list = []
        for record in rs:
            list.append({'survey_id':record[0],'s_seq':record[1],'question':record[2],'a1':record[3],'a2':record[4],'a3':record[5], 'a4':record[6], 'in_date':record[7],'in_user_id':record[8],'up_date':record[9],'up_user_id':record[10],'in_user_name':record[11]})
        return list
    
    
    def myinsert(self,survey_id, s_seq, question, a1, a2, a3, a4, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (survey_id, s_seq, question, a1, a2, a3, a4, in_user_id, up_user_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

        
    def myupdate(self,survey_id, s_seq, question, a1, a2, a3, a4, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")        
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (question, a1, a2, a3, a4, up_user_id, survey_id, s_seq))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    
    def mydelete(self,survey_id, s_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")  
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (survey_id, s_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()
        
        
if __name__ == "__main__":
    dao = MyDaoSdetail()

    
    
    