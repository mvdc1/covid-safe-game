// Function to sort scoreboard in an ascending order.
function sortByProperty(property){  
    return function(a,b){
        if(a[property] > b[property])  
            return 1;
        else if(a[property] < b[property])
            return -1;
        return 0;  
    };
}

// Function to update scores.
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
        var data = await res.json();
        return data.sort(sortByProperty("total"));
    } catch (error) {
        return "An error has occurred because 'scores.json' is currently unavailable.";
    }
}

// Calling the score updating function through a separate function due to asynchronous functions requiring the function to be caught through '.then()'.
function callScores() {
    getScores().then(function (x) {
        if(x == "An error has occurred because 'scores.json' is currently unavailable.") {
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

// Setting time interval so scores update every 3 seconds.
var interval = window.setInterval(callScores, 3000);