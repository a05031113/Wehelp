let model=document.getElementById('h');
let btn=document.getElementById('btn');

// 右側欄顯示
btn.onclick=function() {
    model.style.display="block";
}
// 右側欄消失
window.onclick=function(){
    if (event.target==model){
        model.style.display="none";
    }
}

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

let promotion = document.querySelectorAll(".boxPromotion")
let box = document.querySelectorAll(".box")

// 讀取json資料
fetch(url).then(function(response){
    return response.json();
}).then(function(lis){
    let data = lis["result"]["results"];
    // promotion's pic
    for (let i=0; i<promotion.length; i++){
        const figPromotion = document.createElement("img");
        figPromotion.className = "proPic";
        let file=data[i]['file'].split("https");
        figPromotion.src = "https"+file[1];
        promotion[i].appendChild(figPromotion);
    }
    // promotion's content
    for (let i=0; i<promotion.length; i++){
        const Pro = document.createElement("div");
        Pro.className = "desPromotion"
        const textnode = document.createTextNode(data[i]["stitle"]);
        Pro.appendChild(textnode);
        promotion[i].appendChild(Pro);
    }
    // title's pic
    for (let i=0; i<box.length; i++){
        const fig = document.createElement("img");
        fig.className = "pic";
        let file=data[i+2]['file'].split("https");
        fig.src = "https"+file[1];
        box[i].appendChild(fig);
    }
    // titles's content
    for (let i=0; i<box.length; i++){
        const text = document.createElement("div");
        text.className = "description"
        const textnode = document.createTextNode(data[i+2]["stitle"]);
        text.appendChild(textnode);
        box[i].appendChild(text);
    }
})

// load more
let more = document.querySelectorAll(".titlesMore");
let noneBtn = document.querySelector(".more");
let i=0;
// onclick funciton
moreBtn.onclick=function() {
    more[i].style.display="block";
    if (i>=more.length-1){
        noneBtn.style.visibility="hidden";
    }
    i++
}


