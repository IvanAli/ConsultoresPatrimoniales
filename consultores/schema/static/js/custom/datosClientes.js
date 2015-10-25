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