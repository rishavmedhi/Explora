#!/usr/bin/python
import cgi,cgitb
import MySQLdb
import datetime
import json
cgitb.enable()
print "Content-Type: text/html\n"
dic={}
try:
	fs=cgi.FieldStorage()
	pid=fs.getvalue("pid")
	curstat=fs.getvalue("curstat")
	oldstat=fs.getvalue("oldstat")
	db=MySQLdb.connect("localhost","root","1","project_analyser")
	con=db.cursor()
	if str(oldstat)==str(curstat):
		dic["Status"]=0;
	elif curstat=="Abandoned" and oldstat=="Completed" or curstat=="Completed" and oldstat=="Abandoned":
		sql="UPDATE `projects` SET `status`='%s' WHERE `id`='%s';"%(str(curstat),str(pid))
		con.execute(sql)
		db.commit()
		dic["Status"]=1;
	elif curstat=="Completed" and oldstat!="Abandoned" or curstat=="Abandoned" and oldstat!="Completed":
		sql="UPDATE `projects` SET `status`='%s' WHERE `id`='%s';"%(str(curstat),str(pid))
		con.execute(sql)
		db.commit()
		sql="SELECT `faculty` FROM `projects` WHERE `id`='%s';"%(str(pid))
		con.execute(sql)
		res=con.fetchone()
		#print res[0]
		sql="UPDATE `faculty` SET `Projects`=`Projects`-1 WHERE `Faculty_Name`='%s';"%(str(res[0]))
		con.execute(sql)
		db.commit()
		dic["Status"]=1;
	elif curstat=="Ongoing":
		sql="SELECT `faculty` FROM `projects` WHERE `id`='%s';"%(str(pid))
		con.execute(sql)
		res=con.fetchone()
		sql="SELECT `Projects` FROM `faculty` WHERE `Faculty_Name`='%s';"%(str(res[0]))
		con.execute(sql)
		res1=con.fetchone()
		if(int(res1[0])<10):
			sql="UPDATE `faculty` SET `Projects`=`Projects`+1 WHERE `Faculty_Name`='%s';"%(str(res[0]))
			con.execute(sql)
			db.commit()
			sql="UPDATE `projects` SET `status`='%s' WHERE `id`='%s';"%(str(curstat),str(pid))
			con.execute(sql)
			db.commit()
			dic["Status"]=1;
		else:
			dic["Status"]=2;
except:
	dic["Status"]=0;
print json.dumps(dic)
