$.ajax({
	url:"/cgi-bin/explora/teacherdata.py",
	type:"POST",
	success:function(data){
		var retjson=JSON.parse(data);
		$("#faculty").append("<option default>Select Faculty</option>");
		$.each(retjson["teachers"],function(index,element){
			$("#faculty").append("<option>"+element+"</option>");
		});
	}
});
//localStorage.setItem("tagid_remove","");
$(document).ready(function(){
	$("#msg").css("display","none");
	$("#tagbtn").on("click",function(event){
		$("#titleerror").html("")
		$("#domainerror").html("")
		$("#descerror").html("")
		$("#teammemerror").html("")
		$("#contacterror").html("")
		$("#facultyerror").html("")
		$("#abserror").html("");
		if($("#title").val().trim().length==0)
		{
			$("#titleerror").css("color","red");
			$("#titleerror").append("    *Please Enter Title of The Project");
		}
		if($("#domain").val().trim().length==0)
		{
			$("#domainerror").css("color","red");
			$("#domainerror").append("    *Please Enter Domain of The Project");
		}
		if($("#description").val().trim().length==0)
		{
			$("#descerror").css("color","red");
			$("#descerror").append("    *Please Enter One Line Description of The Project");
		}
		if($("#teammem").val().trim().length==0)
		{
			$("#teammemerror").css("color","red");
			$("#teammemerror").append("    *Please Enter Team Member Details with Name and Register Numbers");
		}
		if($("#email").val().trim().length==0 || $("#mobile").val().trim().length==0)
		{
			$("#contacterror").css("color","red");
			$("#contacterror").append("    *Please Enter Contact Details of the Team Leader");
		}
		if($("#faculty").val()==="Select Faculty")
		{
			$("#facultyerror").css("color","red");
			$("#facultyerror").append("    *Please Select Appropriate Faculty");
		}
		var abstract=$("#abstract").val().trim();
		var title=$("#title").val().trim();
		if(abstract.length==0)
		{
			$("#abserror").append("     *Please Enter Abstract to Start Tagging");
			$("#abserror").css("color","red");
		}
		else
		{
			$("#tags").html("");
			$.ajax({
				url:"/cgi-bin/explora/tagdata.py",
				data:{"abstract":abstract,"title":title},
				type:"POST",
				success:function(data){
					$("#msg").css("display","");
					var json=JSON.parse(data);
					console.log(json["tags"])
					//$("#tags").append('<span class="tag label label-info" id="mytag"><span>'+json[]+'</span><a><i class="remove glyphicon glyphicon-remove-sign glyphicon-white" id="tag"></i></a></span>');
					var li=[]
					$.each(json["tags"],function(value){
						$("#tags").append('<span class="tag label label-success" id="mytag'+value+'"><span>'+json["tags"][value]+'</span><a><i class="remove glyphicon glyphicon-remove-sign glyphicon-white" id="tag'+value+'"></i></a></span>');
						li.push(json["tags"][value]);
					});
					//localStorage.setItem("tagid_present",JSON.stringify(li));
				}
			});
		}
	event.preventDefault();
	});
	$(document).on("click","[id^=tag]",function(){
		var id1=$(this).attr("id").replace("tag","");
		//var c=JSON.parse(localStorage.getItem("tagid_present"));
		//c.splice(c.indexOf($("#mytag"+id1).text()),1);
		//localStorage.setItem("tagid_present",JSON.stringify(c));
  		$("#mytag"+id1).html("");
  		$("#mytag"+id1).prop("id","bewakoof");
  	});
  	$("#submit-button").on("click",function(){
  		var title=$("#title").val().trim();
  		var domain=$("#domain").val().trim();
  		var desc=$("#description").val().trim();
  		var abstract=$("#abstract").val().trim();
  		var faculty=$("#faculty").val();
  		var teammem=$("#teammem").val().trim();
  		var email=$("#email").val().trim();
  		var mobile=$("#mobile").val().trim();
  		var m=[]
  		$("#tags").children().each(function(n, i){ 
  				if(this.id!="bewakoof")
  				{
  					m.push($("#"+this.id).text())
  				}
  		});
  		$.ajax({
  			url:"/cgi-bin/explora/project_upload.py",
			type:"POST",
			data:{"title":title,"domain":domain,"desc":desc,"abstract":abstract,"faculty":faculty,"teammem":teammem,"email":email,"mobile":mobile,"tags":JSON.stringify(m)},
			success:function(data){
			var json=JSON.parse(data);
			localStorage.setItem("id",json["id"]);
			}
  		});
  	});
  	$("#close").on("click",function(){
  		var m=localStorage.getItem("id");
  		localStorage.removeItem("id");
  		window.open("../pages/test.html?id="+m,"_blank");
  	});
});
