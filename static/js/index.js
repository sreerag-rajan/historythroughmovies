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



const imgcarasoul = ["http://127.0.0.1:8000/media/posters/Agantuk.jpg",
    "http://127.0.0.1:8000/media/posters/Apollo_13.jpg",
    "http://127.0.0.1:8000/media/posters/Ek_Doctor_Ki_Maut.jpg",
    "http://127.0.0.1:8000/media/posters/Fires_of_Kuwait.jpg",
    "http://127.0.0.1:8000/media/posters/Koyaanisqatsi.jpg",
    "http://127.0.0.1:8000/media/posters/loandbeholdposter.jpg",
    "http://127.0.0.1:8000/media/posters/Modern_Times.jpg",
    "http://127.0.0.1:8000/media/posters/Pom_Poko.jpg",
    "http://127.0.0.1:8000/media/posters/The_Imitation_Game.jpg",
    "http://127.0.0.1:8000/media/posters/Tutankhamun_cfB1rdN.jpg",
    "http://127.0.0.1:8000/media/posters/The_War_Game.jpg",
    "http://127.0.0.1:8000/media/posters/The_Wind_Rises.jpg",
    "http://127.0.0.1:8000/media/posters/Those_Magnificent_Men_in_Their_Flying_Machines.jpg",
    "http://127.0.0.1:8000/media/posters/Turksib-film-images-c6870e91-beea-4f54-b86c-34827ea86bd.jpg"
]
let i =1

let carasouling = setInterval(()=>{
    if(i===imgcarasoul.length){
        i=0;
    }
    let img =document.getElementById("postercarasoul");
    img.src = imgcarasoul[i];
    i++
},1800)

carasouling();



