/*function checaSeguro(id) {
	select = document.getElementById("select");
    document.getElementById("forma").innerHTML=document.getElementById(id).innerHTML;
}*/

function checaSeguro(id) {
	select = document.getElementById("select");
	for(i = 0; i < select.length; i++) document.getElementById(select.options[i].value).style.display = "none";
	document.getElementById(id).style.display = "block";
}
