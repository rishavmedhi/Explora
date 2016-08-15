$(document).ready(function(){
var token=localStorage.getItem("token");
$.ajax({
url:"/cgi-bin/explora/faculty.py",
data:{"token":token},
type:"POST",
success:function(data){
var json=JSON.parse(data);
$("#name").html("");
$(document).prop("title",json["name"]+" - SRM University");
$("#name").append("<b>"+json["name"]+"</b>");
$("#email").append("<b>("+json["email"]+")</b>");
$("#pc").append("Projects Count:- <b>"+json["pc"]+"</b>");
if(json["pc"]===0)
{
	$("#tab").html("");
}
var p=json["projects"]
$.each(p,function(value){
	var temp=JSON.parse(p[value]);
	$("#tabbody").append('<tr id='+value+'><th scope="row">'+temp["id"]+'</th><td id=p'+temp["id"]+'><a target="_blank" href="../pages/test.html?id='+temp["id"]+'">'+temp["name"]+'</a></td><td>'+temp["domain"]+'</td><td>'+temp["leadmail"]+'</td><td>'+temp["leadmobile"]+'</td><td style="color:green" id="s'+temp["id"]+'">'+temp["status"]+'</td><td><button class="btn btn-danger" data-toggle="modal" data-target="#myModal2" id="'+temp["id"]+'">Change Status</button></td>')
});
}
});
$("#signout").on("click",function(){
localStorage.removeItem("token");
});
$("#close").on("click",function(){
location.href="../pages/loginfaculty.html";
});
$("#changepwd").on("click",function(){
var oldpwd=$("#oldpwd").val().trim()
var newpwd=$("#newpwd").val().trim()
var token=localStorage.getItem("token");
$.ajax({
url:"/cgi-bin/explora/changepwd.py",
data:{"oldpwd":oldpwd,"newpwd":newpwd,"token":token},
type:"POST",
success:function(data){
$("#msg").html("");
$("#msg").append(data);
setTimeout( function() { $("#myModal1").modal( "hide" ) }, 2000 );
}
});
});
$("#myModal1").on("hidden.bs.modal", function(){
    $("#msg").html("");
    $("#msg").append('<p style="font-size: 18px;"><b>Old Password:  </b><input type="password" id="oldpwd" required></p>');
    $("#msg").append('<p style="font-size: 18px;"><b>New Password:  </b><input type="password" id="newpwd" required></p>');
});
$(document).on("click",'button[id^=CS]',function() {
	var id1=$(this).attr("id")
	$("#msg1").html("");
	$("#msg1").append('<p style="font-size: 18px;" id="pid" ><b>Project Id:  </b>'+id1+'</p>');
	$("#msg1").append('<p style="font-size: 18px;" id="pname" ><b>Project Name:  </b>'+$("#p"+id1).text()+'</p>');
	$("#msg1").append('<p style="font-size: 18px;" id="oldstat"><b>Old Status:  </b>'+$("#s"+id1).text()+'</p>');
	$('#msg1').append('<p style="font-size:18px;"><b>New Status: </b><select id="curstat"><option default>Select</option><option>Ongoing</option><option>Completed</option><option>Abandoned</option></select></p>');
});
$("#changestatus").on("click",function(){
var pid=$("#pid").text().replace("Project Id:","").trim();
var curstat=$("#curstat").val();
var oldstat=$("#oldstat").text().replace("Old Status:","").trim();
$.ajax({
url:"/cgi-bin/explora/changestatus.py",
data:{"pid":pid,"curstat":curstat,"oldstat":oldstat},
type:"POST",
success:function(data){
	var json=JSON.parse(data)
	if(json["Status"]==1)
		$("#s"+pid).text(curstat);
	else if(json["Status"]==2)
		alert("Your Ongoing Project Limit is Already 10");
	else
		alert("Changing Status Failed !! Please Try Again Later");
}
});
});
});
