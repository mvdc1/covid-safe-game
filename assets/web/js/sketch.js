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
    try {
        var res = await fetch("scores.json?date=" + Date.now(), {
            headers: {
                "Cache-Control": "no-cache"
            }
        },
        {
            cache: "no-cache"
        });
        return await res.json().sort(sortByProperty("total"));
    } catch (error) {
        return "An error has occurred since 'scores.json' is currently unavailable.";
    }
}

function callScores() {
    getScores().then(function (x) {
        if (x == "An error has occurred since 'scores.json' is currently unavailable.") {
            return;
        } else {
            var str = "<ul>";
            for(var i in x) {
                str += '<li><i class="fas fa-long-arrow-alt-right fa-xs"></i>' + x[i].time + '</li>';
            }
            str += "</ul>";
            document.getElementById("list").innerHTML = str;
        }
    });
}

var interval = window.setInterval(callScores, 3000);