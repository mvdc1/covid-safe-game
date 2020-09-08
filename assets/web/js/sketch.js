function sortByProperty(property){  
    return function(a,b){
        if(a[property] > b[property])  
            return 1;
        else if(a[property] < b[property])
            return -1;
        return 0;  
    };
}

async function getScores() {
    var cd = Date.now();
    const res = await fetch("scores.json?date=" + cd, {headers: {"Cache-Control": "no-cache"}}, {cache: "no-cache"});
    const data = await res.json();
    const sorted = data.sort(sortByProperty("total"));
    return sorted;
}

function callScores() {
    getScores().then(x => {
        var str = "<ul>";
        for(var i in x) {
            str += '<li><i class="fas fa-long-arrow-alt-right fa-xs"></i>' + x[i]['time'] + '</li>';
        }
        str += "</ul>";
        document.getElementById("list").innerHTML = str;
    });
}

var interval = window.setInterval(callScores, 3000);