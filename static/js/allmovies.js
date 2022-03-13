
const url = window.location.href.split("?");
const base = url[0];
const query = url[1];
const usp = new URLSearchParams(query);
console.log(url)
console.log(usp.toString())

document.getElementById("sort").addEventListener("change",()=>{
    let sortby = document.getElementById("sort").value;
    console.log(sortby)
    usp.set('sort',sortby);
    usp.set("page",1);
    window.location.href = base + "?" +usp.toString()  
})



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
    usp.set("page",1)   
    
    window.location.href = base + "?" +usp.toString()
    
})


function gotopage(num){
    usp.set("page",num);
    window.location.href = base + "?" +usp.toString()
}