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

