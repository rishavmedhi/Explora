#!/usr/bin/python
import cgi,cgitb
import MySQLdb
import json
cgitb.enable()

print "Content-Type: text/html\n"
db=MySQLdb.connect("localhost","root","1","project_analyser")
cursor=db.cursor(MySQLdb.cursors.DictCursor)

fs=cgi.FieldStorage()
query=fs.getvalue("q")
param=fs.getvalue("params")

result={}
resultlist=[]
x={}
if int(param)==1:
	query1="%"+query+"%"
	sql="select `id`,`name`,`desc`,`domain` from `projects` where `name` like '%s';"%(query1)
elif int(param)==2:
	query1="%"+query+"%"
	sql="select `id`,`name`,`desc`,`domain` from `projects` where `domain` like '%s';"%(query1)
elif int(param)==3:
	query1="%"+query+"%"
	sql="select `id`,`name`,`desc`,`domain` from `projects` where `faculty` like '%s';"%(query1)
elif int(param)==4:
	query1=query
	#yet to  be coded     similarity based algo
res=cursor.execute(sql)
for p in cursor:
	x={}
	x["id"]=p["id"]
	x["name"]=p["name"]
	x["domain"]=p["domain"]
	x["desc"]=p["desc"]
	resultlist.append(x)
result={"result":resultlist}
print json.dumps(result)
