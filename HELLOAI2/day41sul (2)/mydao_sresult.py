import cx_Oracle
import mybatis_mapper2sql
from day41sul.mylog import MyLog

class MyDaoSresult:
    def __init__(self):
        self.conn = cx_Oracle.connect('python/python@localhost:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_sresult.xml')[0]
        
    def myselect(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        MyLog().getLogger().debug(sql)
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            list.append({'survey_id':record[0],'s_seq':record[1],'st_mobile':record[2],'answer':record[3], 'in_date':record[4],'in_user_id':record[5],'up_date':record[6],'up_user_id':record[7]})
        return list
    
    def myselect_graph(self,survey_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_graph")
        MyLog().getLogger().debug(sql)
        rs = self.cs.execute(sql, (survey_id,))
        list = []
        for r in rs:
            list.append({'survey_id':r[0],'s_seq':r[1],'question':r[2],'a1':r[3],'a2':r[4],'a3':r[5],'a4':r[6],'c1':r[7],'c2':r[8],'c3':r[9],'c4':r[10]})
        return list    
    
    
    def myinsert_ans(self,survey_id, st_mobile, ans):
        anses = ans.split(",")
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "merge")
        MyLog().getLogger().debug(sql)
        
        for idx,a in enumerate(anses):
            self.cs.execute(sql, (survey_id, idx+1, st_mobile, a))
        
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt    
    
    def myinsert(self,survey_id, s_seq, st_mobile, answer, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (survey_id, s_seq, st_mobile, answer, in_user_id, up_user_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

        
    def myupdate(self,survey_id, s_seq, st_mobile, answer, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")        
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (answer, up_user_id, survey_id, s_seq, st_mobile))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    
    def mydelete(self,survey_id, s_seq, st_mobile):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")  
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (survey_id, s_seq, st_mobile,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()
        
        
if __name__ == "__main__":
    dao = MyDaoSresult()

    
    
    