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
        // promotion's content
        const Pro = document.createElement("div");
        Pro.className = "desPromotion"
        const textnode = document.createTextNode(data[i]["stitle"]);
        Pro.appendChild(textnode);
        promotion[i].appendChild(Pro);
    }
    // title's pic
    let boxCount=0;
    for (let i=0; i<box.length;i++) {
        const fig = document.createElement("img");
        fig.className = "pic";
        let file=data[boxCount+2]['file'].split("https");
        fig.src = "https"+file[1];
        box[boxCount].appendChild(fig);
        // titles's content
        const text = document.createElement("div");
        text.className = "description"
        const textnode = document.createTextNode(data[boxCount+2]["stitle"]);
        text.appendChild(textnode);
        box[boxCount].appendChild(text);
        boxCount++
    }

    let noneBtn = document.querySelector(".more");
    let body = document.querySelector("body");
    let titleCount = 2
    // onclick funciton
    moreBtn.onclick=function() {
        // add title*2
        for (let i=0; i<2; i++){
            const text = document.createElement("div");
            text.className = "title"
            const textnode = document.createTextNode("");
            text.appendChild(textnode);
            body.insertBefore(text, noneBtn);
        }
        // add box into added title1
        let title = document.querySelectorAll(".title");
        for(let i=0; i<4; i++){
            let addBox = document.createElement("div");
            addBox.className = "box"
            let boxnode = document.createTextNode("");
            addBox.appendChild(boxnode);
            title[titleCount].appendChild(addBox);   
        }
        titleCount++
        // add box into added title2
        for(let i=0; i<4; i++){
            let addBox = document.createElement("div");
            addBox.className = "box"
            let boxnode = document.createTextNode("");
            addBox.appendChild(boxnode);
            title[titleCount].appendChild(addBox);   
        }
        titleCount++;
        // if boxcount > data count => hide the buttom
        if (boxCount+8>=data.length-2){
            noneBtn.style.visibility="hidden"
        }
        // add pic and content into box
        let box = document.querySelectorAll(".box")
        for (let i=0; i<box.length;i++) {
            const fig = document.createElement("img");
            fig.className = "pic";
            let file=data[boxCount+2]['file'].split("https");
            fig.src = "https"+file[1];
            box[boxCount].appendChild(fig);
            // titles's content
            const text = document.createElement("div");
            text.className = "description"
            const textnode = document.createTextNode(data[boxCount+2]["stitle"]);
            text.appendChild(textnode);
            box[boxCount].appendChild(text);
            boxCount++
        }
    }
})