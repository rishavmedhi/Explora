function abc()
{
$("#validate").on('submit',function(event) {
var query=$("#search-box").val();
var selected = $("input[type='radio'][name='stype']:checked").val()
		$.ajax({
			url:"/cgi-bin/explora/psearch.py",
			data:{"q":query,"params":selected},
			type:"POST",
			success:function(data){
				var result=JSON.parse(data);
				$(".sresults").remove();
				$("#sbody").css("visibility","visible");
				if(result["result"]==0)
				{
					$("#sbody").append('<div class="sresults"><p style="text-align:center;color:red">No Search Results found</p></div>')
				}
				else{
				$.each(result["result"],function(index,element){
					$("#sbody").append('<div class="sresults"><a href="../pages/test.html?id='+element["id"]+'" target="_blank"><h2><b>'+element["name"]+'</b></h2></a><p class="domain">'+element["domain"]+'</p><p class="pdescription">'+element["desc"]+'</p></div>');
				});
				}}});
event.preventDefault();
});
}
$(document).ready(function(){
	$("#validate").on("keypress",function(e){
if(e.keyCode===13){
abc();
}
});	
$("#search-btn").on("click",abc)
});
