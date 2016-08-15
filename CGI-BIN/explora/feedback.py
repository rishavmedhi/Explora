#!/usr/bin/python
import cgi,cgitb
import MySQLdb
import json
cgitb.enable()
dic={}
print "Content-Type: text/html\n"
db=MySQLdb.connect("localhost","root","1","project_analyser")
con=db.cursor()
fs=cgi.FieldStorage()
n=fs.getvalue("n")
e=fs.getvalue("e")
m=fs.getvalue("m")
sql="INSERT INTO `feedback` (`name`,`email`,`message`) VALUES('%s','%s','%s');"%(str(n),str(e),str(m))
con.execute(sql)
db.commit()
