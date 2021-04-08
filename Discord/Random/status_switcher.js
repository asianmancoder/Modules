/*
This module was originally created by a friend of mine... it's pretty cool!!
*/

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
