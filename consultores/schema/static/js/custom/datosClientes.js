var clic = 1;
function mostrar(){ 
   if(clic==1){
   document.getElementById("direccion").style.display = 'block';
   clic = clic + 1;
   } else{
       document.getElementById("direccion").style.display = 'none';      
    clic = 1;
   }   
}

function errorEmail(){ 
	var email =document.getElementById("email")
	if (email==""){
	document.getElementById("errorEmail1").style.display = 'block';
	document.getElementById("errorEmail2").style.display = 'none'; 
	 
	}else {
	document.getElementById("errorEmail1").style.display = 'none';
	document.getElementById("errorEmail2").style.display = 'block';  
	}
}