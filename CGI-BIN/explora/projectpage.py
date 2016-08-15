#!/usr/bin/python
import cgi,cgitb
import MySQLdb
import datetime
import json
cgitb.enable()
print '''Content-Type: text/html\n
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Explora, SRM University</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">


    <!-- Bootstrap Core CSS -->
    <link href="../startbootstrap-sb-admin-2-1.0.8/bower_components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- MetisMenu CSS -->
    <link href="../startbootstrap-sb-admin-2-1.0.8/bower_components/metisMenu/dist/metisMenu.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="../startbootstrap-sb-admin-2-1.0.8/dist/css/sb-admin-2.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="../startbootstrap-sb-admin-2-1.0.8/bower_components/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">

    <link rel="stylesheet" href="style.css" type="text/css">
	<link href="../Ravalic/css/lightbox.css" rel="stylesheet">
	<link href='http://fonts.googleapis.com/css?family=Poppins:400,600,700,500,300' rel='stylesheet' type='text/css'>
	<link href='http://fonts.googleapis.com/css?family=Roboto:400,900italic,900,700italic,700,400italic,500,500italic,300,100italic,100,300italic' rel='stylesheet' type='text/css'>
    
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>
<header>
	<div class="container" style="width:100%;background-color:black;">
		<div class="row">
			<div class="col-md-4 ">
				<div class="navbar-header">
					    <button type="button" class="navbar-toggle menu-button" data-toggle="collapse" data-target="#myNavbar">
					        <span class="glyphicon glyphicon-align-justify"></span>
					    </button>
      					<a class="navbar-brand logo" href="#" style="color:red;">Explora</a>
    			</div>
			</div>
			<div class="col-md-8">
				<nav class="collapse navbar-collapse" id="myNavbar" role="navigation">
					<ul class="nav navbar-nav navbar-right menu">
							<li><a href="http://localhost/Ravalic/index.html" class="page-scroll active">Home</a></li>
							<li><a href="http://localhost/startbootstrap-sb-admin-2-1.0.8/pages/search.html" class="page-scroll">Search</a></li>
							<li><a href="http://localhost/startbootstrap-sb-admin-2-1.0.8/pages/myform.html" class="page-scroll">Register</a></li>
							<!--li><a href="#section4" class="page-scroll">Contact</a></li-->
					</ul>
				</nav>
			</div>
		</div>
	</div>
</header>
<div id="page-wrapper">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-12">
                        <h1 class="page-header" id="heading"></h1>
         		<h4 id="status"></h4>
                    </div>
                    <div class="col-lg-12" id="restbody">
         	    </div>
         	 </div>
       	     </div>
</div>
<!-- jQuery -->
    <script src="../startbootstrap-sb-admin-2-1.0.8/bower_components/jquery/dist/jquery.min.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="../startbootstrap-sb-admin-2-1.0.8/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

    <!-- Metis Menu Plugin JavaScript -->
    <script src="../startbootstrap-sb-admin-2-1.0.8/bower_components/metisMenu/dist/metisMenu.min.js"></script>

    <!-- Custom Theme JavaScript -->
    <script src="../startbootstrap-sb-admin-2-1.0.8/dist/js/sb-admin-2.js"></script>
    
    <script src="../startbootstrap-sb-admin-2-1.0.8/js/pgdata2.js"></script>

</body>
</html>'''

#mysql connection
db=MySQLdb.connect("localhost","root","1","project_analyser")
cursor=db.cursor(MySQLdb.cursors.DictCursor)

fs=cgi.FieldStorage()
id=fs.getvalue("id")
#id="CS50"
ans_json={}
sql="SELECT * from `projects` where `id`='%s';"%(id)
res=cursor.execute(sql)
#results=cursor.fetchone()
#titles=["id","name","domain","desc","abstract","faculty","team_mem","contact","status","date"]
for row in cursor:
	c=row
	break
	
c["date"]=str(c["date"])
#del c["modified_desc"]
#print json.dumps(c)		
