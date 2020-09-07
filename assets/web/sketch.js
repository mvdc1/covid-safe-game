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
    const res = await fetch("scores.json");
    const data = await res.json();
    const sorted = data.sort(sortByProperty("total"));
    return sorted;
}

getScores().then(x => {
    var str = "<ul>";
    for(var i in x) {
        str += "<li>" + x[i]["time"] + "</li>";
    }
    str += "</ul>";
    document.getElementById("list").innerHTML = str;
});