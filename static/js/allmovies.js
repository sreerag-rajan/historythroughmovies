
document.getElementById("sort").addEventListener("change",()=>{
    let sortby = document.getElementById("sort").value;
    window.location.href= `/allmovies/${sortby}`;
})