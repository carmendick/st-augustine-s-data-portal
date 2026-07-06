document.querySelectorAll(".stat-card h2").forEach((item)=>{

    if(isNaN(item.innerText)) return;

    let end=parseInt(item.innerText);

    let start=0;

    let speed=Math.max(10, Math.floor(800/end));

    const counter=setInterval(()=>{

        start++;

        item.innerText=start;

        if(start>=end){

            clearInterval(counter);

        }

    },speed);

});