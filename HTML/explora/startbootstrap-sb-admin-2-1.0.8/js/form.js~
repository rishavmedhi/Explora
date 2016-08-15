$(document).ready(function(){	
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
	$("#validate").on('submit',function(event) {
	$("#submit-button").on("click",function(event){
		var pname=$("#title").val();
		var pdomain=$("#domain").val();
		var pdesc=$("#description").val();
		var pabstract=$("#abstract").val();
		var pfaculty=$("#faculty").val();
		var pteam1=$("#t-name1").val();
		var pteam2=$("#t-name2").val();
		var pteam3=$("#t-name3").val();
		var pteammem=pteam1+", "+pteam2+", "+pteam3;
		var pleadmail=$("#email").val();
		var pleadmob=$("#mobile").val();
		var submitdata={"pname":pname,"pdomain":pdomain,"pdesc":pdesc,"pabstract":pabstract,"pfaculty":pfaculty,"pteammem":pteammem,"pleadmail":pleadmail,"pleadmob":pleadmob};
		//console.log(submitdata);
		$.ajax({
		url:"/cgi-bin/explora/project_upload.py",
		type:"POST",
		data:submitdata,
		success:function(data){
			var json=JSON.parse(data);
			window.open("../pages/test.html?id="+json["id"],"_blank");
		}
		});
	
		
});
event.preventDefault();
});
});	
