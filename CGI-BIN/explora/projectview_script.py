#!/usr/bin/python
import cgi,cgitb
import MySQLdb
import datetime
import json
cgitb.enable()
print "Content-Type: text/html\n"
#mysql connection
db=MySQLdb.connect("localhost","root","1","project_analyser")
cursor=db.cursor(MySQLdb.cursors.DictCursor)

fs=cgi.FieldStorage()
id=fs.getvalue("id")
#id="CS50"
ans_json={}
sql="SELECT * from `projects` where `id`='%s';"%(id)
res=cursor.execute(sql)
#results=cursor.fetchone()
#titles=["id","name","domain","desc","abstract","faculty","team_mem","contact","status","date"]
for row in cursor:
	c=row
	break
	
c["date"]=str(c["date"])
#del c["modified_desc"]
print json.dumps(c)
		
