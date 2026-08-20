const overlay =
document.getElementById("commandOverlay");


const input =
document.getElementById("commandInput");


const results =
document.getElementById("commandResults");



if(!overlay || !input || !results){
    console.log("Spotlight elements missing");
}
else{


/* =========================
   OPEN / CLOSE
========================= */


function openCommand(){

    overlay.style.display="flex";

    input.focus();

}


function closeCommand(){

    overlay.style.display="none";

    input.value="";

    results.innerHTML="";

}



/* =========================
   KEYBOARD SHORTCUT
========================= */


document.addEventListener(
"keydown",
(e)=>{


    if(
        (e.ctrlKey || e.metaKey)
        &&
        e.key.toLowerCase()==="k"
    ){

        e.preventDefault();

        openCommand();

    }



    if(e.key==="Escape"){

        closeCommand();

    }


});





/* =========================
   SEARCH
========================= */


input.addEventListener(
"input",
async()=>{


let q=input.value.trim();



if(q.length < 2){

    results.innerHTML="";

    return;

}



try{


let response =
await fetch(
`/api/command-search?q=${encodeURIComponent(q)}`
);



let videos =
await response.json();



results.innerHTML="";



videos.forEach(video=>{


let item=document.createElement("div");


item.className="command-item";



item.innerHTML=`

<img 
class="command-thumb"
src="/watch/thumbnail/${video.thumbnail}"
>



<div class="command-info">

<h6>
${video.title}
</h6>


<small>

${video.category || "Video"}

•
${video.views || 0} views

</small>


</div>

`;



item.onclick=()=>{


saveSearch(video.title);


window.location =
"/watch/"+video.id;


};



results.appendChild(item);



});



}

catch(error){

console.error(
"Spotlight search error:",
error
);

}


});





/* =========================
   RECENT SEARCHES
========================= */


let history =
JSON.parse(
localStorage.getItem("streamHistory")
||
"[]"
);



function saveSearch(value){


if(!history.includes(value)){


history.unshift(value);


history =
history.slice(0,5);



localStorage.setItem(
"streamHistory",
JSON.stringify(history)

);


}


}



}