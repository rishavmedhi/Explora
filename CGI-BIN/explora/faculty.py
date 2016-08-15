#!/usr/bin/python
import cgi,cgitb
import MySQLdb
import datetime
import json
import base64
from Crypto.Cipher import AES
key=AES.new("explora123456789")
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
token=fs.getvalue("token")
recv=base64.decodestring(token)
email=key.decrypt(recv)
email=email.strip()
db=MySQLdb.connect("localhost","root","1","project_analyser")
con=db.cursor()
sql="SELECT * FROM `faculty` WHERE `Faculty_Mail`='%s';"%(str(email))
con.execute(sql)
res=con.fetchall()
name=res[0][1]
email=res[0][2]
dic={}
dic["name"]=name
dic["email"]=email
dic["pc"]=res[0][4]
sql1="SELECT `id`,`name`,`domain`,`leadmail`,`leadmobile`,`status` FROM `projects` WHERE `faculty` LIKE '%s';"%(str(name))
con.execute(sql1)
r=con.fetchall()
p=[]
for i in r:
	d={}
	d["id"]=i[0]
	d["name"]=i[1]
	d["domain"]=i[2]
	d["leadmail"]=i[3]
	d["leadmobile"]=i[4]
	d["status"]=i[5]
	p.append(json.dumps(d))
dic["projects"]=p
print json.dumps(dic)
