
document.getElementById("sort").addEventListener("change",()=>{
    //There is a select tag that sends sort values when an option is selected
    let sortby = document.getElementById("sort").value;
    
    //Seperating the base from the query section
    let url = window.location.href.split("?");
    let base = url[0]
    let querystr = url[1]
    
    //checking to see if any prior queries are there or not, i.e. whether sort or category selection has been performed before or not
    if(querystr){
        //If we are coming in here that means there were some previous queries.
        
        //Now sorting query needs to be found and updated while leaving catagory query alone. This is also becaues we don't know if the user chose to filter first or sort first
        let queries = querystr.split("&");
        let sort_found_index = null
        for(let i =0; i<queries.length; i++){
            if(queries[i].includes("sort=")){
                sort_found = true;
                sort_found_index=i;
            }
        }   
        
        //adding the previous queries that were not a sorting one
        url = base + "?";        
        for(let i =0; i<queries.length;i++){
            if(i!==sort_found_index){
                url= url+"&"+queries[i];
                //The "&" here is not really required as the page only takes either category or sort, but this is incase more keys are added later
            }
        }

        //adding the new sorting query
        window.location.href = url+"&sort="+sortby;        
    }
    else{
        //if there had been no previous querires just add a sorting one
        window.location.href = base + "?" + "sort="+sortby
    }   
})