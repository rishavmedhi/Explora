$(document).ready(function(){
	var winurl=window.location.href;
	var pgid=winurl.split("=");
	pgid=pgid.pop();
	$.ajax({
	url:"/cgi-bin/explora/projectview_script.py",
	data:{id:pgid},
	type:"POST",
	success:function(data){
	//console.log(data);
	var json=JSON.parse(data);
	//console.log(json);
	//console.log(o);
	//console.log(a);
	$("#heading").append("<center>"+json["name"]+"</center>");
	$("#restbody1").append("<p><b>Tags </b> :");
	var m=JSON.parse(json["tags"]);
	$.each(m,function(value){
		$("#restbody1").append('<span class="tag label label-success"><span>'+m[value]+'</span><a><i class="glyphicon glyphicon-white"></i></a></span>');
	});
	$("#restbody1").append("</p><br/>");
	$("#restbody").append("<br /><br /><p><b>Started Date : </b>"+json["date"]+"</p><br/>");
	$("#restbody").append("<p><b>Description : </b>"+json["desc"]+"</p><br/>");
	$("#restbody").append("<p><b>Domain</b> : "+json["domain"]+"</p><br/>");
	$("#restbody").append("<p><b>Guiding Faculty</b> : "+json["faculty"]+"</p><br/>");
	$("#restbody").append("<p><b>Team Members </b> : "+json["team_mem"]+"</p><br/>");
	$("#restbody").append("<p><b>Abstract </b> : "+json["abstract"]+"</p><br/>");
	$("#restbody").append("<p><b>Email </b> : "+json["leadmail"]+"</p><br/>");
	$("#restbody").append("<p><b>Mobile </b> : "+json["leadmobile"]+"</p><br/>");
	var o=json["status"]
	$("#status").append("<center><p><b>Status </b> : "+json["status"]+"</p></center><br/>");
	if(o=="Ongoing")
	{
		$("#status").css("color","green");
	}
	else if(o=="Completed")
	{
		$("#status").css("color","red");
	}
	else
	{
		$("#status").css("color","blue");
	}
	}
	});});
