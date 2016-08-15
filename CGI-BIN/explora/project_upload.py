#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
name=fs.getvalue("title")
domain=fs.getvalue("domain")
desc=fs.getvalue("desc")
desc=MySQLdb.escape_string(desc)
abstract=fs.getvalue("abstract")
abstract=MySQLdb.escape_string(abstract)
faculty=fs.getvalue("faculty")
team=fs.getvalue("teammem")
leadmail=fs.getvalue("email")
leadmob=fs.getvalue("mobile")
tags=fs.getvalue("tags")
status="Ongoing"
list_of_words = [i.lower() for i in wordpunct_tokenize(str(desc)) if i.lower() not in stop_words]
list_of_words=list(set(list_of_words))
mdesc=" ".join(list_of_words)
db=MySQLdb.connect("localhost","root","1","project_analyser")# connection to mysql with root as username and 1 as password and database project_analyser
con=db.cursor()
sql="SELECT COUNT(*) FROM projects;"
con.execute(sql)
res=con.fetchone()
r=int(res[0])
r=r+1;
id1="CS"+str(r)
sql="INSERT INTO `projects`(`id`,`name`,`domain`,`desc`,`modified_desc`,`abstract`,`tags`,`faculty`,`team_mem`,`leadmail`,`leadmobile`,`status`) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(str(id1),str(name),str(domain),str(desc),str(mdesc),str(abstract),str(tags),str(faculty),str(team),str(leadmail),str(leadmob),str(status))
con.execute(sql)
db.commit()
sql="UPDATE `faculty` SET `Projects`=`Projects`+1 WHERE `Faculty_Name`='%s';"%(str(faculty))
con.execute(sql)
db.commit();
print json.dumps({"id":id1})
