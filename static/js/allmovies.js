// const url = window.location.href.split("?");
// const base = url[0];
// const query = url[1];
// const usp = new URLSearchParams(query);
// console.log(usp.toString())

// document.getElementById("sort").addEventListener("change",()=>{
//     let sortby = document.getElementById("sort").value;
//     usp.set('sort',sortby);
//     usp.set("page",1);
//     window.location.href = base + "?" +usp.toString()  
// })

let count = 0;
document.getElementById("filterdivopener").addEventListener("click",()=>{
    count++;
    if(count%2!==0){
        document.getElementById("filterdivopener").textContent="Close"
        document.getElementById("filter").style.display = "block";
    document.getElementById("filter").style.transition = "200ms";
    }
    else{
        document.getElementById("filterdivopener").textContent="Filter"
        document.getElementById("filter").style.display = "none";
        document.getElementById("filter").style.transition = "200ms";
    }
    
    
})

document.querySelector("#filterbtn").addEventListener("click",()=>{
    let catfilter = []
    let langfilter = [];
    let categories = document.getElementsByClassName("category")
    let languages = document.getElementsByClassName("language");

    for(cat of categories){
        if(cat.checked){
            if(cat.value==="all"){
                break;
            }
            catfilter.push(cat.value);
        }
    }
    for(lang of languages){
        if(lang.checked){
            if(lang.value==="all"){
                break;
            }
            langfilter.push(lang.value);
        }
    }
    console.log(catfilter,langfilter)
    if(catfilter.length>0){
        usp.set("category",catfilter.join("_"));
    }
    else{
        usp.delete("category")
    }
    if(langfilter.length>0){
        usp.set("language",langfilter.join("_"))
    }
    else{
        usp.delete("language")
    }   
    
    window.location.href = base + "?" +usp.toString()
    
})






//------------------------------------------------------------------------------------------
// document.getElementById("sort").addEventListener("change",()=>{
//     //There is a select tag that sends sort values when an option is selected
//     let sortby = document.getElementById("sort").value;
    
//     //Seperating the base from the query section
//     let url = window.location.href.split("?");
//     let base = url[0]
//     let querystr = url[1]
    
//     //checking to see if any prior queries are there or not, i.e. whether sort or category selection has been performed before or not
//     if(querystr){
//         //If we are coming in here that means there were some previous queries.
        
//         //Now sorting query needs to be found and updated while leaving catagory query alone. This is also becaues we don't know if the user chose to filter first or sort first
//         let queries = querystr.split("&");
//         let sort_found_index = null
//         for(let i =0; i<queries.length; i++){
//             if(queries[i].includes("sort=")){
//                 sort_found = true;
//                 sort_found_index=i;
//             }
//         }   
        
//         //adding the previous queries that were not a sorting one
//         url = base + "?";        
//         for(let i =0; i<queries.length;i++){
//             if(i!==sort_found_index){
//                 url= url+"&"+queries[i];
//                 //The "&" here is not really required as the page only takes either category or sort, but this is incase more keys are added later
//             }
//         }

//         //adding the new sorting query
//         window.location.href = url+"&sort="+sortby;        
//     }
//     else{
//         //if there had been no previous querires just add a sorting one
//         window.location.href = base + "?" + "sort="+sortby
//     }   
// })