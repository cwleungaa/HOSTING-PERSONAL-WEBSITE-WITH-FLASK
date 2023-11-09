function redirect_page(tab_name){
   window.location.assign(tab_name);
}


// Date function
function date(){
    var date1 = new Date();
    document.getElementById("date").innerHTML = date1.getDate()+"/"+ (date1.getMonth()+1) +"/" + date1.getFullYear();
}





