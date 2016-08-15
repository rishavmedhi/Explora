#!/usr/bin/python
import cgi,cgitb
import MySQLdb
import json
import base64
from Crypto.Cipher import AES
key=AES.new("explora123456789")
cgitb.enable()
print "Content-Type: text/html\n"
dic={}
#MySQL connection
db=MySQLdb.connect("localhost","root","1","project_analyser")
con=db.cursor()
fs=cgi.FieldStorage()
email=fs.getvalue("username")
password=fs.getvalue("password")
sql="SELECT COUNT(*) FROM `faculty` WHERE `Faculty_Mail`='%s' AND `Faculty_pwd`='%s';"%(str(email),str(password))
con.execute(sql)
res=con.fetchone()
if int(res[0])!=0:
	dic["status"]="success"
	sql="SELECT `Faculty_Name` FROM `faculty` WHERE `Faculty_Mail`='%s' AND `Faculty_pwd`='%s';"%(str(email),str(password))
	con.execute(sql)
	res=con.fetchone()
	dic["name"]=str(res[0])
	temp=len(email)
	temp1=temp%16
	res=16-temp1
	for i in range(0,res):
		email=email+" "
	token=key.encrypt(email)
	dic["token"]=base64.encodestring(token)
else:
	dic["status"]="fail"
print json.dumps(dic)
