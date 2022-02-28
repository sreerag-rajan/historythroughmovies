document.getElementById("themes").addEventListener("click",()=>{
    window.location.href = "/themes"
})
document.getElementById("countries").addEventListener("click",()=>{
    window.location.href = "/countries"
})
document.getElementById("specialModules").addEventListener("click",()=>{
    window.location.href = "/special-modules"
})
document.getElementById("otherResources").addEventListener("click",()=>{
    window.location.href = "/other-resources"
})
document.getElementById("allmovies").addEventListener("click",()=>{
    window.location.href = "/allmovies"
})
document.querySelector("#workingon").addEventListener("mouseover",()=>{
    document.getElementById("wo1").style.display="none";
    document.getElementById("wo2").style.display="flex"

});
document.querySelector("#workingon").addEventListener("mouseout",()=>{
    document.getElementById("wo1").style.display="flex";
    document.getElementById("wo2").style.display="none"

});
document.querySelector("#recentmid").addEventListener("mouseover",()=>{
    document.getElementById("rt1").style.display="none";
    document.getElementById("rt2").style.display="flex"

});
document.querySelector("#recentmid").addEventListener("mouseout",()=>{
    document.getElementById("rt1").style.display="flex";
    document.getElementById("rt2").style.display="none"

});



let i =1
if(posterarr.length>0){
    setInterval(()=>{
        if(i===posterarr.length){
            i=0;
        }
        let img =document.getElementById("postercarasoul");
        // img.src = imgcarasoul[i];
        img.src = posterarr[i];
        i++
    },1800)

}



// carasouling();



