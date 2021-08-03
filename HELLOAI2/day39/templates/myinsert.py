import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cs = conn.cursor()
sql = "insert into tetris (LEARN400,ACTION) values (:1,:2)"



cs.execute(sql,('9','5'))


cs.close()
conn.commit()
conn.close()