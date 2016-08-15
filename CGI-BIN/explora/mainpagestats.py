#!/usr/bin/python
import cgi,cgitb
import MySQLdb
import json
cgitb.enable()
dic={}
print "Content-Type: text/html\n"
db=MySQLdb.connect("localhost","root","1","project_analyser")
con=db.cursor()
sql="SELECT COUNT(*) FROM `faculty` WHERE `Projects`<10;"
con.execute(sql)
res=con.fetchone()
dic["faculty"]=int(res[0])
sql="SELECT COUNT(*) FROM `projects`;"
con.execute(sql)
res=con.fetchone()
dic["projects"]=int(res[0])
sql="SELECT COUNT(*) FROM `projects` WHERE `status`='Ongoing';"
con.execute(sql)
res=con.fetchone()
dic["ongoing"]=int(res[0])
sql="SELECT COUNT(*) FROM `projects` WHERE `status`='Completed';"
con.execute(sql)
res=con.fetchone()
dic["completed"]=int(res[0])
print json.dumps(dic)
