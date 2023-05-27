#MySQL/MariaDB Connection.
import MySQLdb
host = "localhost"
user = "aplicacao"
password = "senha"
db = "Escola"
port = 3306
con = MySQLdb.connect(host,user,password,db,port)

cur = con.cursor()
#cur = con.cursor(MySQLdb.cursors.DictCursor) to return Dict.

#CRUD Creation
def select(fields, tables, where=None):
	
	global cur
	
	query = "SELECT " + fields + " FROM " + tables
	if (where):
		query = query + " WHERE " + where
	
	cur.execute(query)
	return cur.fetchall() #Tupla.


# print(select("Nome, CPF", "Aluno")) READ






