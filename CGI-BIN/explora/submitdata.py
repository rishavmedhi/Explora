#!/usr/bin/python
import cgi,cgitb
import MySQLdb
import json
cgitb.enable()
print "Content-Type: text/html\n"

#MySQL connection
db=MySQLdb.connect("localhost","root","1","project_analyser")
cursor=db.cursor(MySQLdb.cursors.DictCursor)

try:
	sql="SELECT  `id` FROM  `projects` ORDER BY  `id` DESC LIMIT 1;"
	res=cursor.execute(sql)
	for row in cursor:
		x=row["id"] 
	fs=cgi.FieldStorage()
	#print fs
	pid=int(x)+1
	pname=fs.getvalue("pname")
	pdomain=fs.getvalue("pdomain")
	pdesc=fs.getvalue("pdesc")
	pabstract=fs.getvalue("pabstract")
	pfaculty=fs.getvalue("pfaculty")
	pteammem=fs.getvalue("pteammem")
	pleadmail=fs.getvalue("pleadmail")
	pleadmob=fs.getvalue("pleadmob")
	status="Ongoing"
	sql1="insert into `projects`(`id`,`name`,`domain`,`desc`,`abstract`,`faculty`,`team_mem`,`contact`,`status`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(str(pid),pname,pdomain,pdesc,pabstract,pfaculty,pteammem,pleadmob,status)
	cursor.execute(sql1)
	db.commit()
	db.close()
	#print sql1
	#retjson={"id":pid}
	print pid
	
	#	print "success"

except Exception as e:
	print e
	print "Error"
