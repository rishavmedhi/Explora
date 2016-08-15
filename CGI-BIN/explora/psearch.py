#!/usr/bin/python
import cgi,cgitb
import MySQLdb
import json
cgitb.enable()

print "Content-Type: text/html\n"
db=MySQLdb.connect("localhost","root","1","project_analyser")
cursor=db.cursor(MySQLdb.cursors.DictCursor)
cursor1=db.cursor()

def tokenizer(query):
	#removal of punctuations
	x=query
	punc=[",",":",";","'",".","(",")","[","]","{","}","<",">","?","@","!",'"',"|"]
	for i in punc:
		x=x.replace(i," ").replace("\n","").replace("-"," ")
	
	#tokenising queries
	x=x.replace("    "," ")
	x=x.replace("   "," ")
	x=x.replace("  "," ")
	x=x.split(" ")
	return x

def facultysearch(query):	
	#getting tokens
	x=tokenizer(query)
	
	#finding appropriate records
	tags=set()
	for i in range(0,len(x)):
		k=i
		sql="select `id` from `projects` where `%s` like '%s';" %("faculty","%"+str(x[k]).lower()+"%")
		cursor1.execute(sql)
		res=cursor1.fetchall()
		uni=set(list(res))
		if len(tags)==0:
			tags=tags.union(uni)
		else:
			tags=tags.intersection(uni)	
	final=[]
	for i in tags:
		final.append(i[0])

	final.sort()
	return final

def domainsearch(query):
	x=tokenizer(query)
	
	#removing stop words
	sql1="select `COL 2` from `stopwords`;"
	cursor1.execute(sql1)
	stop=cursor1.fetchall()
	stop=list(stop)
	stoplist=[]
	for i in stop:
		if i[0]!="development":
			stoplist.append(i[0])
	
	y=[]
	for i in x:
		if i.lower().strip() in stoplist or len(i)==1 or len(i)==0:
			continue
		y.append(i)
	x=y
	#finding records
	tags=set()
	for i in range(0,len(x)):
		k=i
		sql="select `id` from `projects` where `%s` like '%s';" %("domain","%"+str(x[k]).lower()+"%")
		cursor1.execute(sql)
		res=cursor1.fetchall()
		uni=set(list(res))
		tags=tags.union(uni)
	final=[]
	for i in tags:
		final.append(i[0])

	final.sort()
	return final
def similarsearch(query):
	x=tokenizer(query)
	sql1="select `COL 2` from `stopwords`;"
	cursor1.execute(sql1)
	stop=cursor1.fetchall()
	stop=list(stop)
	stoplist=[]
	for i in stop:
		if i[0]!="development":
			stoplist.append(i[0])
	y=[]
	for i in x:
		if i.lower().strip() in stoplist or len(i)==1 or len(i)==0:
			continue
		y.append(i)
	x=y
	tags=set()
	for i in range(0,len(x)):
		k=i
		sql="select `id` from `projects` where `%s` like '%s';" %("name","%"+str(x[k]).lower()+"%")
		cursor1.execute(sql)
		res=cursor1.fetchall()
		uni=set(list(res))
		if len(tags)==0:
			tags=tags.union(uni)
		else:
			tags=tags.intersection(uni)
	final=[]
	for i in tags:
		final.append(i[0])
	final.sort()
	if(len(final)!=0):
		sql="SELECT `tags` from `projects` where `id`='%s';"%(str(final[0]))
		cursor1.execute(sql)
		r=cursor1.fetchone();
		r=eval(r[0])
		finalset=set();
		for i in r:
			sql="SELECT `id` from `projects` where `tags` like '%s';"%("%"+str(i)+"%")
			cursor1.execute(sql)
			res1=cursor1.fetchall()
			temp=set(list(res1))
			finalset=finalset.union(temp)
	f=[]
	for j in finalset:
		f.append(j[0])
	f.sort()
	return f
fs=cgi.FieldStorage()
query=fs.getvalue("q")
param=fs.getvalue("params")

result={}
resultlist=[]
resultid=[]
x={}
if int(param)==1:
	query1="%"+query+"%"
	sql="select `id`,`name`,`desc`,`domain` from `projects` where `name` like '%s';"%(query1)
elif int(param)==2:
	resultid=domainsearch(query)
elif int(param)==3:
	resultid=facultysearch(query)
elif int(param)==4:
	query1="% "+query+" %"
	sql="select `id`,`name`,`desc`,`domain` from `projects` where `abstract` like '%s';"%(query1)
elif int(param)==5:
	resultid=similarsearch(query)
if int(param)==1 or int(param)==4:
	res=cursor.execute(sql)
	for p in cursor:
		x={}
		x["id"]=p["id"]
		x["name"]=p["name"]
		x["domain"]=p["domain"]
		x["desc"]=p["desc"]
		resultlist.append(x)	

if int(param)==3 or int(param)==2 or int(param)==5:
	for i in resultid:
		x={}
		sql="select `id`,`name`,`desc`,`domain` from `projects` where `id` like '%s';"%(i)
		cursor.execute(sql)
		res=cursor.fetchone()
		x["id"]=res["id"]
		x["name"]=res["name"]
		x["domain"]=res["domain"]
		x["desc"]=res["desc"]
		#print x
		resultlist.append(x)
	
result={"result":resultlist}
print json.dumps(result)
