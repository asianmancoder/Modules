const authToken = "u not 'gon see dis";
const statuses = ["Add your statuses here"]


function random(list) {
    return list[Math.floor(Math.random() * list.length)];
}

function setStatus(status) {

    let Http = new XMLHttpRequest();
    let url = 'https://discord.com/api/v8/users/@me/settings';
    let data = JSON.stringify({
        "custom_status": {
            "text": status
        }
    });
    Http.open("PATCH", url);
    Http.setRequestHeader("authorization", authToken);
    Http.setRequestHeader("Content-Type", "application/json");
    Http.send(data);
    Http.onload = function() {
        //console.log("Status changed to: " + status);
    }
}

setInterval(function() {
    setStatus(random(statuses));
}, 10000); 


// The above version was written by my friend Jess.
// This is my version, formatted my way:


const statuses = ["Add your statuses here"];

let authtoken = "not safe to post";
let content_type = "application/json";

setInterval(function() {
    let request = new XMLHttpRequest();
    let url = "https://discord.com/api/v9/users/@me/settings";
    // Snowflake format, I think.
    let data = JSON.stringify({
        "custom_status": {
            "text": statuses[Math.floor(Math.random() * 10)]
        }
    });
    
    request.open("PATCH", url);
    request.setRequestHeader("authorization", authtoken);
    request.setRequestHeader("Content-Type", content_type);
    request.send(data);
}, 10000);
