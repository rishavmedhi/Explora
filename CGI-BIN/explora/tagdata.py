#!/usr/bin/python
import cgi,cgitb
import MySQLdb
import json
cgitb.enable()
print "Content Type: text/html\n"

db=MySQLdb.connect("localhost","root","1","project_analyser")
cursor=db.cursor()

def keywords(x,param):
	x=x.replace("    "," ")
	x=x.replace("   "," ")
	x=x.replace("  "," ")
	x=x.split(" ")
	

	#removal of puctuation
	y=[]
	
	sql1="select `COL 2` from `stopwords`;"
	cursor.execute(sql1)
	stop=cursor.fetchall()
	stop=list(stop)
	stoplist=[]
	for i in stop:
		stoplist.append(i[0])

	for i in x:
		if i.lower().strip() in stoplist or len(i)==1 or len(i)==0:
			continue
		y.append(i)
	x=y
	#print x

	tags=set()
	for i in range(0,len(x)):
		k=i
		if param=="t":
			addon="limit 2"
		else:
			addon=""
		sql="select `id` from `microsoft_terms` where `term` like '%s' %s;" %(str(x[k]).lower()+"%",str(addon))
		cursor.execute(sql)
		res=cursor.fetchall()
		uni=set(list(res))
		if k+2<len(x):
			sql="select `id` from `microsoft_terms` where `term` like '%s';" %("%"+str(x[k]).lower()+"%")
			cursor.execute(sql)
			res=cursor.fetchall()
			a=set(list(res))
			#print a
			sql="select `id` from `microsoft_terms` where `term` like '%s';" %("%"+str(x[k+1]).lower()+"%")
			cursor.execute(sql)
			res=cursor.fetchall()
			b=set(list(res))
			#print b
			sql="select `id` from `microsoft_terms` where `term` like '%s';" %("%"+str(x[k+2]).lower()+"%")
			cursor.execute(sql)
			res=cursor.fetchall()
			c=set(list(res))
			#print c
			tri=set(a.intersection(b.intersection(c)))
			#print tri
			bi=set((a.intersection(b)).union(b.intersection(c)))
			#print bi
			final=set(tri.union(bi))
			#print final			
			if(len(final)!=0):
				tags=tags.union(final)
		tags=tags.union(uni)	
		#print tags
	final=[]
	for i in tags:
		#print i[0]
		final.append(int(i[0]))

	final.sort()
	#print final[0:30]
	return final
	
def idval(final):
	final_tag=[]
	for i in final:
		sql="select `term` from `microsoft_terms` where `id`='%s';" %(i)
		cursor.execute(sql)
		res=cursor.fetchall()
		final_tag.append(res[0][0])
	return final_tag

#main part
punc=[",",":",";","'",".","(",")","[","]","{","}","<",">","?","@","!",'"',"|"]
fs=cgi.FieldStorage()
x=fs.getvalue("abstract")
title=fs.getvalue("title")

#removal of bigrams
sql="select `COL4` from `bigram`;"
cursor.execute(sql)
res=cursor.fetchall()
res=list(res)

for i in res:
	x=x.lower().replace(i[0],"")
	title=title.lower().replace(i[0],"")

#punctuation removal
for i in punc:
	x=x.replace(i," ").replace("\n","").replace("-"," ")
	title=title.replace(i," ").replace("\n","").replace("-"," ")

title_list=keywords(title,"t")
abstract_list=keywords(x,"a")

temp=[]

if (len(abstract_list)>30):
	abstract_list=abstract_list[0:30]

for i in title_list:
	if i not in abstract_list:
		temp.append(i)

if len(temp)!=0:
	title_list=temp		

if(len(title_list)>20):
	title_list=title_list[0:20]

#Combining both the list contents in abstract_list
for i in title_list:
	abstract_list.append(i)
abstract_list.sort()
final_list=idval(abstract_list)
ret={"tags":final_list}
print json.dumps(ret)
