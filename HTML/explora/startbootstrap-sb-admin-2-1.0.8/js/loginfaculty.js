function abc()
{
$("#validate").on('submit',function(event) {
var formData={
		  'username'              : $('input[name=username]').val(),
          'password'             : $('input[name=password]').val(),
          };
$.ajax({
url:"/cgi-bin/explora/facultylogin.py",
data:formData,
type:"POST",
success:function(data){	
	var json=JSON.parse(data);
	if(json["status"]=="fail")
	{
		$("#errormsg").html("");
		$("#errormsg").append("Authentication Failure!! Please Try Again");
	}
	if(json["status"]=="success")
	{
		$("#errormsg").html("");
		$("#errormsg").append("Welcome "+json["name"]);
		localStorage.setItem("token",json["token"]);
		location.href="../pages/facultyprofile.html";
	}
}
});
event.preventDefault();
});
}
$(document).ready(function(){
$("#validate").on("keypress",function(e){
if(e.keyCode===13){
abc();
}

});
$("#login").on("click",abc);

});
